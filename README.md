

_**A general purpose development environment template for the generation of Python modules & packages.**_  
_**Utilizing many of my favourite development tools and deployable with the cookicutter module.**_ 


![](assets/pydough.png)

# 🌟 Features

---

The following tool is mandatory (you will thank me later):
* [**pip-tools**][pip-tools-url] -  Pins every single package dependency (even the dependency’s dependencies).

All the following features are optional:

* [**flake8**][flake8-url] - linting wrapper that glues together pycodestyle, pyflakes & mccabe.
* [**black**][black-url] - code formatter.
* [**mypy**][mypy-url] - for static type checking.
* [**pre-commit**][pre-commit-url] - a framework for managing pre-commit hooks (pre-configured with many hooks).
* [**isort**][isort-url] - organizes imports automatically.
* [**bandit**][bandit-url] -  finds common security issues .
* [**sphinx**][sphinx-url] -  for creating documentation.
* [**click**][click-url] -  for creating Command line interfaces.
* [**invoke**][invoke-url] - Common package maintenance tasks are automated using a module I have written with this python library.


## Other Features

* Automatically configures git message template.
* Selection of licenses to choose from (or vist [**choosealicense.com**](https://choosealicense.com/) for more choices).
* Optionally include the following:
  - [**python-semantic-release**](https://github.com/relekang/python-semantic-release) or [**bump2version**][bump2version-url] - version control and release.
  - [**commitizen**][commitizen-url] - for parsing and enforcing descriptive git commits.
  - [**cruft**][cruft-url] - project boilerplate is maintained in sync with parent cookiecutter template. 
  - [**safety**][safety-url] - check dependencies for known security vulnerabilities.
  - [**flakeheaven**][flakeheaven-url] - Flake8 wrapper to replace flakehell.
* Included are GitHub actions for codeql-analysis, CICD/tests and dependabot.
* Option to specify Docstring style ([**Google**][docstring-google] or [**numpy**][docstring-numpy] - see [**pep 257**][pep257-url] and [**sphinx**][docstring-sphinx]).
* Optionally include a configuration file (toml, ini, json or yaml).
* Optionally include resource files (e.g. sqlite3, pickle, png).
* Option to include Logging using the dictConfig() configuration.
* Automatically include badges based on your selections e.g.:

[![pre-commit][pre-commit-image]][pre-commit-url]
[![Imports: isort][isort-image]][isort-url]
[![Code style: black][black-image]][black-url]
[![Checked with mypy][mypy-image]][mypy-url]
[![security: bandit][bandit-image]][bandit-url]

# 📋 Pre-Installation Requirements

---

- [X] Python >= 3.8.
- [X] [**Git**](https://git-scm.com/) must be installed
- [X] An activated virtual environment. (I prefer [**virtualenv**][virtualenv-url] with [**virtualenv-wrapper**][virtualenvwrapper-url]).
- [X] [**Cookiecutter**][cookiecutter-url] package installed into the virtual environment (or use [**pipx**][pipx-url]).
```bash
$ pip install cookiecutter
```
- [X] [**jinja2-time**](https://pypi.org/project/jinja2-time/) installed into the virtual environment.
```bash
$ pip install jinja2-time
```




# 💾 Installation

---

Assuming you are at the command prompt of the activated virtual environment
simply type the following:

```bash
$ cookiecutter https://github.com/stephen-ra-king/pydough
```

cookiecutter will prompt you for a selection of inputs and eventually [**pip-tools**][pip-tools-url] will
pin your dependencies from the inputs you have given.

When the installation script has finished it would be prudent to check the following log for any errors:

**logs / post_gen.log**

This template uses [**layered requirements**][layered-url] (the default being "development")
so now install the packages using pip-tools as follows:

```bash
$ pip-sync <package-name>/requirements.txt
```
The following is ***no longer required*** as pip-tools is installed by default.

```bash
$ pip install -r <package-name>/requirements.txt
```


# ⚙️ Optional Post-Installation steps

---

> :question: The majority of the following steps are automated by a **post_installation.py** file that I have written.
> However this file is removed by the **post_gen_project.py** hook if the name you have used is not 
> "Stephen-RA-King".  I have configured it this way as I use the [**keyring**][keyring-url] library to store my 
> API keys.  This way I have automated the entire environment creation.  If you feel this is something that
> you would like to do, then feel free to configure this file to your needs.

### Recommended Post Installation Requirements:
You will need accounts and API keys with the following services: 
- [GitHub](http://github.com)
- [Read the Docs](https://readthedocs.org/)
- [TestPyPi](https://test.pypi.org/)
- [PyPi](https://pypi.org/)

The following services can be linked to your github account (settings > integrations > applications)
   - [Codecov.io](https://about.codecov.io/)
   - [Codefactor.io](https://www.codefactor.io/)
   - [Deepsource.io](https://deepsource.io/)
   - [Pre-commit.ci](https://pre-commit.ci/)

### Finalization Steps

1. Put your pypi and testpypi keys into the .pypirc file.
2. Create a remote repository on GitHub.
3. If using GitHub actions - Add your PyPi and TestPyPi tokens to the repository actions secrets with the following variable names:
   - TEST_PYPI_API_TOKEN
   - PYPI_API_TOKEN
4. If you are using Python Semantic Release, create the following environment variables:
   - GH_TOKEN = _GitHub token_
   - REPOSITORY_PASSWORD = _PyPI token_
   - REPOSITORY_USERNAME = \__token__
5. Import the GitHub repository into [**Read the Docs**](https://readthedocs.org/).
6. Install your package as an "editable" package.

Editable installs were not possible until 2021, but that has been remedied by [**pep 660**][pep660-url].
This can be performed by either 'pip' or 'setuptools'
```sh
$ python -m pip install -e . 
```
or
```sh
$ python setup.py develop
```
7. Push the local files to GitHub

Note Git is automatically initialized and the following is automatically run by the post install hook
```sh
$ git remote add origin git@github.com:<user>/<repository-name>.git 
```
So simply add, commit and push
```sh
$ git add *
$ git commit -m "chore: initial commit"
$ git push -u origin main 
```
Note: If you chose to use the [**pre-commit**][pre-commit-url] package then many hooks (e.g. Flake8, Black, Bandit Prettier etc.)
will now download and configure themselves and eventually be run against each file in the repository.
This may take some time and some files may get modified. You will need to "git add" these files again.

8. Again when the time comes create a git tag (optionally signed) and push to the remote
```sh
$ git tag -s 0.1.0 -m "chore: 0.1.0 tag"
$ git push --tags
```

9. Create build artefacts with the following command:
```sh
$ python -m build
```
10. Now upload the build artefacts to the test repository for final testing:
```sh
$ python -m twine upload --config-file .pypirc -r testpypi dist/*
```

11. When the time comes, release to the main repository:
```sh
$ python -m twine upload --config-file .pypirc dist/*
```

12. If you are using services codecov.io, codefactor.io
and deepsource.io then you will need to login to those services with your GitHub account and import your respositories

### Note
Some badges can take up to 24 Hrs to update (yes download badge ... I am looking at you). So please be patient.

# 📝 Using the template Features

---

### Python Semantic Release
If you opted to use PSR then the future uploading to GitHub & uploading to PyPI, 
will be done automatically.
After you have committed changes to git, issue the following command:
```sh
$ semantic-release publish
```
Publish will do a sequence of things:

- Update changelog file.
- Run semantic-release version.
- Push changes to git.
- Run build_command and upload the distribution file to your repository.
- Run semantic-release changelog and post to your vcs provider.
- Attach the files created by build_command to GitHub releases.

### Documentation
"Read the docs" will automatically generate new documentation when you push to GitHub.
Howver you can manually generate local documenattion by simply moving to the "docs" directory and issuing the make command.
```sh
$ make html
```
You can then open the "...docs/_build/html/index.html" file with a browser.
It is generally best to clear the _build directory when generating new documentation by using the following command
```sh
$ make clean html
```

### Logging
If you have chosen to use logging, then the ABSOLUTE path to the log file will need
to be set.  Currently it is set to a RELATIVE file to where the application is run.
Everybody's file structures are different, so obviously it is not possible for me to 
know where you want your log file to be.

This can be set in the src / __init__.py file  -> handlers -> file -> filename

### Invoke

I have written a "***tasks.py***" file that takes care of many of the mundane repository maintenance tasks:

```shell
inv --list
Available tasks:

  bandit                     Runs bandit against selected python files.
  build                      Creates a new sdist & wheel build using the PyPA tool.
  clean                      Removes all test, build, log and lint artifacts from the environment.
  docs                       Build documentation.
  lint                       Run all lint tasks on 'src' files only.
  lint-all                   Run all lint tasks on all files.
  lint-black (bl, black)     Runs black formatter against selected python files.
  lint-flake8 (fl, flake8)   Run flake8 against selected files.
  lint-isort (is, isort)     Run isort against selected python files.
  mypy                       Run mypy against selected python files.
  psr                        Runs semantic-release publish.
  publish                    Uploads a build to the PyPI-test and PyPI python repositories.
  pypi                       Uploads a build to the PyPI python repository.
  pypi-test                  Uploads a build to the PyPI-test python repository.
  safety                     Runs safety to check for insecure requirements.
  secure                     Runs all security tools.
  tests                      Run tests using pytest.
  update                     Updates the development environment
```


# 📆 Possible future enhancements

---

- Use Ruff to replace Flake8 (plus dozens of plugins), isort, pydocstyle, eradicate,
pyupgrade, and autoflake, all while executing tens or hundreds of times faster.


# 📜 License

Distributed under the MIT license. See [![][license-image]][license-url] for more information.



# <ℹ️> Meta

---

[![](assets/linkedin.png)](https://www.linkedin.com/in/sr-king)
[![](assets/github.png)](https://github.com/Stephen-RA-King)
[![](assets/www.png)](https://stephen-ra-king.github.io/justpython/)
[![](assets/email2.png)](mailto:sking.github@gmail.com) 


Author: Stephen King ([sking.github@gmail.com](mailto:sking.github@gmail.com))


Cookiecutter template: [![pydough][pydough-image]][pydough-url] version: 1.3.4

Digital Object Identifier: [![DOI](https://zenodo.org/badge/453434377.svg)](https://zenodo.org/badge/latestdoi/453434377)


<!-- Markdown link & img dfn's -->
[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[bump2version-url]: https://github.com/c4urself/bump2version
[click-url]: https://github.com/pallets/click/
[commitizen-url]: https://github.com/commitizen-tools/commitizen
[cookiecutter-url]: https://github.com/cookiecutter/cookiecutter
[cruft-url]: https://github.com/cruft/cruft/
[docstring-google]: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[docstring-numpy]: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
[docstring-sphinx]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[flake8-url]: https://github.com/PyCQA/flake8
[flakeheaven-url]: https://github.com/flakeheaven/flakeheaven
[github]: https://github.com/stephen-ra-king/pydough
[google-docstring-url]: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
[invoke-url]: https://www.pyinvoke.org/
[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://github.com/PyCQA/isort
[keyring-url]: https://github.com/jaraco/keyring
[layered-url]: https://github.com/jazzband/pip-tools/#workflow-for-layered-requirements
[license-image]: https://img.shields.io/pypi/l/pynamer
[license-url]: https://github.com/Stephen-RA-King/pydough/blob/main/LICENSE
[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: https://github.com/python/mypy
[numpy-docstring-utl]: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
[pep257-url]: https://peps.python.org/pep-0257/
[pep660-url]: https://peps.python.org/pep-0660/
[pip-tools-url]: https://github.com/jazzband/pip-tools/
[pipx-url]: https://github.com/pypa/pipx
[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[pydough-image]: https://img.shields.io/badge/pydough-2023-orange
[pydough-url]: https://github.com/Stephen-RA-King/pydough
[safety-url]: https://github.com/pyupio/safety
[sphinx-url]: https://github.com/sphinx-doc/sphinx
[virtualenv-url]: https://virtualenv.pypa.io
[virtualenvwrapper-url]: https://pypi.org/project/virtualenvwrapper/
[wiki]: https://github.com/stephen-ra-king/pydough/wiki
