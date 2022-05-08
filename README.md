# Cookiecutter template

_**A general purpose template for the creation of a Python application or library**_


![](https://github.com/Stephen-RA-King/cc_template/raw/main/header.png)


## Template Features

All the following features are optional:

* [**Flake8**][flake8-url] - Tool that glues together pycodestyle, pyflakes & mccabe
* [**Black**][black-url] - Code formatter
* [**MyPy**][mypy-url] - Tool for static type checking
* [**Pre-Commit**][pre-commit-url] - A framework for managing pre-commit hooks (pre-configured with many hooks)
* [**isort**][isort-url] - Sort imports automatically
* [**Bandit**][bandit-url] -  Finds common security issues 
* [**Sphinx**][sphinx-url] -  Package for creating documentation
* [**Click**][click-url] -  Package for creating Command line interfaces

The following tool is mandatory (you will thank me later):
* [**pip-tools**][pip-tools-url] -  Pins every single package dependency (even the dependency’s dependencies)


### Other Features
* Automatically installs pre-commit (if selected) and associated git hook
* Automatically configures git message template
* Selection of licenses to choose from
* Optionally include [**Safety**][safety-url] to check dependencies for known security vulnerabilities
* Optionally include [**Flakeheaven**][flakeheaven-url] Flake8 wrapper to replace flakehell
* Optionally include [**bump2version**][bump2version-url] to maintain version strings in your source code
* Options to specify Docstring style (Google, Numpy or [**PEP257**][pep257-url])
* Optionally include [**Commitizen**][commitizen-url] for parsing and enforcing descriptive commits
* Optionally include Logging using the dictConfig() configuration
* Optionally include an eMail package
* Optionally include badges at specific locations:

[![pre-commit][pre-commit-image]][pre-commit-url]
[![Imports: isort][isort-image]][isort-url]
[![Code style: black][black-image]][black-url]
[![Checked with mypy][mypy-image]][mypy-url]
[![security: bandit][bandit-image]][bandit-url]

## Pre Installation Requirements

1. Python 3.7, 3.8, 3.9 or 3.10
2. Git
3. Virtual Environment. (I like [**virtualenv**][virtualenv-url] with [**virtualenv_wrapper**][virtualenvwrapper-url])
4. [**Cookiecutter**][cookiecutter-url] installed into the Virtual Environment

## Installation

Assuming you are at the command prompt of the activated virtual environment
simply type the following:

```sh
cookiecutter https://github.com/stephen-ra-king/cc_template
```

cookiecutter will prompt you for a selection of inputs and eventually [**pip-tools**][pip-tools-url] will
pin your dependencies from the inputs you have given.
This template uses [**layered requirements**][layered-url] (the default being "development")
so now install the packages using pip as follows:

```sh
pip install -r <package-name>/requirements.txt
```


## Release History

* 1.0.1
    * Work in progress

## Meta

Author: Stephen RA King

Distributed under the License. See ``LICENSE`` for more information.

[https://github.com/https://github.com/stephen-ra-king/cc_template][github]

_For more examples and usage, please refer to the [Wiki][wiki]._



<!-- Markdown link & img dfn's -->
[virtualenv-url]: https://virtualenv.pypa.io
[virtualenvwrapper-url]: https://pypi.org/project/virtualenvwrapper/
[cookiecutter-url]: https://github.com/cookiecutter/cookiecutter
[layered-url]: https://github.com/jazzband/pip-tools/#workflow-for-layered-requirements
[flake8-url]: https://flake8.pycqa.org/en/latest/
[sphinx-url]: https://www.sphinx-doc.org/en/master/
[click-url]: https://click.palletsprojects.com/en/8.0.x/
[commitizen-url]: https://github.com/commitizen-tools/commitizen
[safety-url]: https://github.com/pyupio/safety
[pep257-url]: https://www.python.org/dev/peps/pep-0257/
[bump2version-url]: https://pypi.org/project/bump2version/
[pip-tools-url]: https://pypi.org/project/pip-tools/
[flakeheaven-url]: https://pypi.org/project/flakeheaven/

[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit

[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://pycqa.github.io/isort/

[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black

[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit

[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: http://mypy-lang.org/

[mit-license-image]: https://img.shields.io/badge/license-MIT-blue
[mit-license-url]: https://choosealicense.com/licenses/mit/

[bsd-license-image]: https://img.shields.io/badge/license-BSD-blue
[bsd-license-url]: https://www.openbsd.org/policy.html

[gplv3-license-image]: https://img.shields.io/badge/license-GPLv3-blue
[gplv3-license-url]: https://choosealicense.com/licenses/gpl-3.0/

[apachev2-license-image]: https://img.shields.io/badge/license-Apache%202-blue.svg
[apachev2-license-url]: https://choosealicense.com/licenses/apache-2.0/

[wiki]: https://github.com/stephen-ra-king/cc_template/wiki
[github]: https://github.com/stephen-ra-king/cc_template
