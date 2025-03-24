# Python Project Structuring

This is a cookicutter template for a python project structure, 
following the principles of Clean Code and Domain Driven Designs.


## Cookiecutter

Create projects swiftly from cookiecutters (project templates) with this command-line utility. Ideal for generating Python package projects and more.

## Installation

Install cookiecutter using pip package manager:

```
# pipx is strongly recommended.
pipx install cookiecutter

# If pipx is not an option,
# you can install cookiecutter in your Python user directory.
python -m pip install --user cookiecutter
```

### Use a GitHub template

```
# You'll be prompted to enter values.
# Then it'll create your Python package in the current working directory,
# based on those values.
# For the sake of brevity, repos on GitHub can just use the 'gh' prefix
$ pipx run cookiecutter gh:PaxPrz/Python-Project-Structuring
```

### Use a local template

```
$ pipx run cookiecutter Python-Project-Structuring/
```

### Use it from Python

```
from cookiecutter.main import cookiecutter

# Create project from the cookiecutter-pypackage/ template
cookiecutter('Python-Project-Structuring/')

# Create project from the cookiecutter-pypackage.git repo template
cookiecutter('gh:PaxPrz/Python-Project-Structuring.git')
```