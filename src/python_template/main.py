import os
import string
import subprocess

from cookiecutter.main import cookiecutter
from github import Github
import typer

app = typer.Typer()

SAFE_CHARS = string.ascii_lowercase


class Config:
    def __init__(self, github: Github, repo_name: str, src_dir: str) -> None:
        self._github = github
        user = self._github.get_user()
        self.git_registry = "https://github.com/"
        repo_name = repo_name.lower()
        for ch in repo_name:
            if ch not in SAFE_CHARS:
                repo_name = repo_name.replace(ch, "-")

        self.repo_name = repo_name
        self.project_slug = repo_name.replace("-", "_")
        self.project_name = " ".join(word.capitalize() for word in repo_name.split("-"))
        self.author_email = user.email
        self.author_name = user.name
        self.git_registry_account = user.login
        self.src_dir = src_dir

    def dict(self) -> dict[str, str]:
        return {
            "repo_name": self.repo_name,
            "project_name": self.project_name,
            "project_slug": self.project_slug,
            "author_name": self.author_name,
            "author_email": self.author_email,
            "git_registry": self.git_registry,
            "git_registry_account": self.git_registry_account,
            "src_dir": self.src_dir,
        }


def setup_repo(github: Github, repo_name: str) -> None:
    user = github.get_user()
    user.create_repo(name=repo_name)
    repo = user.get_repo(name=repo_name)
    license_url = f"{repo.url}/community/license/new?branch=master&filename=LICENSE"
    repo.create_issue(
        title="Determine license",
        body=f"Pick a license: {license_url}",
        assignee=user.login,
    )
    os.chdir(repo_name)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", ":tada: Init https://github.com/nymann/python-template"]
    )
    subprocess.run(
        [
            "git",
            "remote",
            "add",
            "origin",
            f"git@github.com:{user.login}/{repo_name}.git",
        ]
    )
    subprocess.run(["git", "push", "-u", "origin", "master"])


@app.command()
def generate(
    github_access_token: str = typer.Option(..., envvar="GITHUB_ACCESS_TOKEN"),
    project_name: str = typer.Option(...),
    src_dir: str = typer.Option("src"),
    template: str = typer.Option("https://github.com/nymann/python-template.git"),
) -> None:
    github = Github(login_or_token=github_access_token)
    config = Config(github=github, repo_name=project_name, src_dir=src_dir)
    cookiecutter(
        template=template,
        extra_context=config.dict(),
        no_input=True,
    )
    setup_repo(github=github, repo_name=config.repo_name)


if __name__ == "__main__":
    app()
