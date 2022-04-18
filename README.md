# Python Package Template

## Usage

```sh
pip install -U cookiecutter

cookiecutter git@github.com:nymann/python-template.git  # if you use ssh
cookiecutter https://github.com/nymann/python-template.git  # if you don't use ssh
```

### Example usage

```sh
$ cookiecutter git@github.com:nymann/python-template.git
# enter the author email, default is mine
author_email [kristian@nymann.dev]:
# enter the author name, default is mine
author_name [Kristian Nymann Jakobsen]:
# enter the git repo url, go create an empty repo (Uncheck Add a README file) and don't add any gitignore or license.
git_url [https://github.com/nymann/repo-name]: https://github.com/nymann/ransom-baby-decryptor
# Enter the project name as snake case, this is fx the package identifier in imports
project_slug [snake_case_repo_name]: ransom_baby_decryptor
# Enter the project name as a Name, this is used in readme and setup.cfg
project_name [Repo Name]: Ransom Baby Decryptor
# I like to have my code inside an src/ directory, you can change the name of this here.
src_dir [src]:
```

After cookiecutter has generated the project, it's time to initialise our git repo.
You can find the instructions to this after creating your project on <https://github.com/new>. However in my case since I use ssh

```sh
# Initialise git project (make sure you are in the correct directory)
git init
# Add all changes
git add .
# Commit them
git commit -m ":tada: Init python-template"
# Add github repo as origin
git remote add origin git@github.com:nymann/python-template.git
# Push them to github on the master branch.
git push -u origin master
```

## Github Actions

If you look inside `.github/workflows` of your generated project, you'll see `package.yml` and `docker-push.yml`, both these files have references to `secrets`. Configure secrets here: <https://github.com/GROUP_OR_USER/YOUR_REPO/settings/secrets/actions>

### Docker

Workflow file: `.github/workflows/docker-push.yml` \
What: Builds a docker image and pushes it to the configured docker registry. \
When: On new git tag

If you are not interesed in this feature, delete the Workflow file.

#### Setup

1. Create a [DockerHub](https://hub.docker.com/) account
2. Go to <https://hub.docker.com/repositories> and Create Repository
3. Go to <https://hub.docker.com/settings/security> and create New Access Token (it needs at least Read and Write permissions)
4. Add two new GitHub secrets: `DOCKER_TOKEN` (the access token you just made) and `DOCKER_USER` (your DockerHub username)

### Pypi

Workflow file: `.github/workflows/package.yml` \
What: Create a package and pushes it to Pypi. \
When: On new git tag

If you are not interesed in this feature, delete the Workflow file.

#### Setup

1. Create a [Pypi](https://pypi.org/) account
2. Api tokens can only be created after the first push of the package.
3. To push it the first time edit `.github/workflows/package.yml`; replace `__token__` with your Pypi username. And add `PYPI_API_TOKEN` to github secrets but set the value to your Pypi password.
4. Create a new tag and push it: `git tag 0.0.1` `git push --tags`
5. If everything went well you should see the project on Pypi, now create an API token on your Pypi project page and overwrite the `PYPI_API_TOKEN` in github secrets with this new token.
6. Revert the changes you made to `.github/workflows/package.yml` (replace username with `__token__`)
