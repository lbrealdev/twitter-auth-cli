# twitter-auth-cli

[![pre-commit](https://github.com/lbrealdev/twitter-auth-cli/actions/workflows/pre-commit.yaml/badge.svg?branch=main&event=push)](https://github.com/lbrealdev/twitter-auth-cli/actions/workflows/pre-commit.yaml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Project setup

Create a new project:
```shell
poetry new <project-name>
```

Activating the virtual environment:
```shell
poetry shell
```

Check pip packages and update:
```shell
pip list

pip install --upgrade pip
```

Add packages dependencies with poetry:
```shell
poetry add click rich pytest requests-oauthlib

or

poetry add $(cat requirements.txt)
```

Add poetry point in pyproject.toml enable for cli:
```toml
[tool.poetry.scripts]
twittercli = "twitter_cli.cli:cli"
```

Install dependencies:
```shell
poetry install
```

After adding the poetry point in pyproject.toml, we can call our cli like this:
```shell
twittercli --help
```


### Run pytest
```shell
poetry run pytest
```