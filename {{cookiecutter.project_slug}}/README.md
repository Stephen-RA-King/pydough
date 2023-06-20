# {{ cookiecutter.project_name }}

> Short blurb about what your product does.

[![PyPI][pypi-image]][pypi-url]
[![Downloads][downloads-image]][downloads-url]
[![Status][status-image]][pypi-url]
[![Python Version][python-version-image]][pypi-url]
[![tests][tests-image]][tests-url]
[![Codecov][codecov-image]][codecov-url]
[![CodeQl][codeql-image]][codeql-url]
{% if cookiecutter.use_docker == 'y' -%}
[![Docker][docker-image]][docker-url]
{%- endif %}
{% if cookiecutter.use_pre_commit == 'y' -%}
[![pre-commit][pre-commit-image]][pre-commit-url]
[![pre-commit.ci status][pre-commit.ci-image]][pre-commit.ci-url]
{%- endif %}
[![readthedocs][readthedocs-image]][readthedocs-url]
[![CodeFactor][codefactor-image]][codefactor-url]
[![Codeclimate][codeclimate-image]][codeclimate-url]
{% if cookiecutter.use_isort == 'y' -%}
[![Imports: isort][isort-image]][isort-url]
{%- endif %}
{% if cookiecutter.use_black == 'y' -%}
[![Code style: black][black-image]][black-url]
{%- endif %}
{% if cookiecutter.use_mypy == 'y' -%}
[![Checked with mypy][mypy-image]][mypy-url]
{%- endif %}
{% if cookiecutter.use_bandit == 'y' -%}
[![security: bandit][bandit-image]][bandit-url]
{%- endif %}
{% if cookiecutter.use_commitizen == 'y' -%}
[![Commitizen friendly][commitizen-image]][commitizen-url]
{%- endif %}
[![Conventional Commits][conventional-commits-image]][conventional-commits-url]
[![DeepSource][deepsource-image]][deepsource-url]
[![license][license-image]][license-url]

One to two paragraph statement about your product and what it does.

![](assets/header_dough.png)

## Installation

---

OS X & Linux:

```sh
pip3 install {{ cookiecutter.project_name }}
```

Windows:

```sh
pip install {{ cookiecutter.project_name }}
```

## Usage example

---

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

---

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
pip install --editable {{ cookiecutter.project_name }}
```

## Documentation

---

[**Read the Docs**](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/)

- [**Example Usage**](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/example.html)
- [**Credits**](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/example.html)
- [**Changelog**](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/changelog.html)
- [**API Reference**](https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/autoapi/index.html)


[**Wiki**](https://github.com/Stephen-RA-King/{{ cookiecutter.project_name }}/wiki)

## Meta

---

{% if cookiecutter.github_username == 'Stephen-RA-King' -%}
[![](assets/linkedin.png)](https://www.linkedin.com/in/sr-king)
[![](assets/github.png)](https://github.com/Stephen-RA-King)
[![](assets/pypi.png)](https://pypi.org/project/{{ cookiecutter.project_name }})
[![Docker](assets/docker.png)](https://hub.docker.com/r/{{ cookiecutter.docker_hub_username }}/{{ cookiecutter.project_name }})
[![](assets/www.png)](https://www.justpython.tech)
[![](assets/email.png)](mailto:sking.github@gmail.com)
{% else %}
[![](assets/github.png)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})
[![](assets/pypi.png)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
{% endif %}

{{cookiecutter.author_name}} : {{cookiecutter.email}}

Distributed under the {{cookiecutter.license}} license. See [![][license-image]][license-url] for more information.

Created with Cookiecutter template: [**pydough**][pydough-url] version 1.3.1


<!-- Markdown link & img dfn's -->

{% if cookiecutter.use_bandit == 'y' -%}
[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit
{%- endif %}
{% if cookiecutter.use_black == 'y' -%}
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
{%- endif %}
[pydough-url]: https://github.com/Stephen-RA-King/pydough
[codeclimate-image]: https://api.codeclimate.com/v1/badges/7fc352185512a1dab75d/maintainability
[codeclimate-url]: https://codeclimate.com/github/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/maintainability
[codecov-image]: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg
[codecov-url]: https://app.codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
[codefactor-image]: https://www.codefactor.io/repository/github/Stephen-RA-King/{{ cookiecutter.project_name }}/badge
[codefactor-url]: https://www.codefactor.io/repository/github/Stephen-RA-King/{{ cookiecutter.project_name }}
[codeql-image]: https://github.com/Stephen-RA-King/{{ cookiecutter.project_name }}/actions/workflows/github-code-scanning/codeql/badge.svg
[codeql-url]: https://github.com/Stephen-RA-King/{{ cookiecutter.project_name }}/actions/workflows/github-code-scanning/codeql
{% if cookiecutter.use_commitizen == 'y' -%}
[commitizen-image]: https://img.shields.io/badge/commitizen-friendly-brightgreen.svg
[commitizen-url]: http://commitizen.github.io/cz-cli/
{%- endif %}
[conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square
[conventional-commits-url]: https://conventionalcommits.org
[deepsource-image]: https://static.deepsource.io/deepsource-badge-light-mini.svg
[deepsource-url]: https://deepsource.io/gh/Stephen-RA-King/{{ cookiecutter.project_name }}/?ref=repository-badge
{% if cookiecutter.use_docker == 'y' -%}
[docker-image]: https://github.com/Stephen-RA-King/pynamer/actions/workflows/docker-image.yml/badge.svg
[docker-url]: https://github.com/Stephen-RA-King/pynamer/actions/workflows/docker-image.yml
{%- endif %}
[downloads-image]: https://static.pepy.tech/personalized-badge/{{cookiecutter.project_name}}?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
[downloads-url]: https://pepy.tech/project/{{cookiecutter.project_name}}
[format-image]: https://img.shields.io/pypi/format/{{ cookiecutter.project_name }}
{% if cookiecutter.use_isort == 'y' -%}
[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://github.com/pycqa/isort/
{%- endif %}
[lgtm-alerts-image]: https://img.shields.io/lgtm/alerts/g/Stephen-RA-King/{{ cookiecutter.project_name }}.svg?logo=lgtm&logoWidth=18
[lgtm-alerts-url]: https://lgtm.com/projects/g/Stephen-RA-King/{{ cookiecutter.project_name }}/alerts/
[lgtm-quality-image]: https://img.shields.io/lgtm/grade/python/g/Stephen-RA-King/{{ cookiecutter.project_name }}.svg?logo=lgtm&logoWidth=18
[lgtm-quality-url]: https://lgtm.com/projects/g/Stephen-RA-King/{{ cookiecutter.project_name }}/context:python
[license-image]: https://img.shields.io/pypi/l/{{cookiecutter.project_name}}
[license-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/main/LICENSE
{% if cookiecutter.use_mypy == 'y' -%}
[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: http://mypy-lang.org/
{%- endif %}
{% if cookiecutter.use_pre_commit == 'y' -%}
[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[pre-commit.ci-image]: https://results.pre-commit.ci/badge/github/Stephen-RA-King/{{ cookiecutter.project_name }}/main.svg
[pre-commit.ci-url]: https://results.pre-commit.ci/latest/github/Stephen-RA-King/{{ cookiecutter.project_name }}/main
{%- endif %}
[pypi-url]: https://pypi.org/project/{{ cookiecutter.project_name }}/
[pypi-image]: https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg
[python-version-image]: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}
[readthedocs-image]: https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest
[readthedocs-url]: https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/?badge=latest
[status-image]: https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg
[tests-image]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions/workflows/tests.yml/badge.svg
[tests-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions/workflows/tests.yml
[wiki]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/wiki

