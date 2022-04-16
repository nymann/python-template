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
