### {{cookiecutter.project_name}}


## Project Installation

If you've installed poetry you can install virtualenv and dependencies using poetry else use pip.


### Using Poetry

Run the following command it will setup the virtualenv

```
poetry install
```

### Using Pip

To install only the packages required for running the app

```
pip install -r requirements.txt
```

If you're a developer to this project, also install the dev requirements

```
pip install -r dev-requirements.txt
```


## Setting up database

You need a SQL database, postgres is preferred. Create a database in your postgres server.
And generate URI link to the database as: `postgresql://{username}:{password}@{ip}:{port}/{database}`

To create new database in postgres using psql:

```
CREATE DATABASE db_name
```


## Setting up the env

Copy the .env.sample file as .env

```
cp .env.sample .env
```

Fill out all the necessary keys.
For the context, `.env` is a configuration file that the app will use to load it's configuration/secrets. It won't be pushed to github repo though.


## Setting up Pre-Commit (If Developer)

Git pre-commit hooks checks your coding practices / bugs / security issues / hard coded keys etc whenever you make a commit to git. If you're a developer, it is a must to maintain code quality of this repo.

Note: You have to install the dev-requirements

To install precommit

```
pre-commit install
```

That's it. Next time you do a commit, it will scan your code and figure out issues. The code won't get pushed until the detected lines are resolved.

If you want to skip this pre-commit test use `-n` while committing

```
git commit -n -m 'message'
```

## Alembic migrations

To run alembic migration:

```
export DATABASE_URI=postgresql://.../test_db
alembic upgrade heads
```

This will create all the tables on test_db
