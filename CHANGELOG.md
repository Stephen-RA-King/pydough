## 1.3.1 (2023-06-20)

### Refactor

- change docker run shell to run exec
- jinja template several hardcoded strings

## 1.3.0 (2023-05-23)

### Feat

- rename the project

### Fix

- add pickle read
- correct shebang for version 3 env

### Refactor

- update numerous jinja2 tags
- add tools and report dirs

## 1.2.2 (2023-04-11)

### Feat

- add support for pickle serialization

### Fix

- **post_gen_project**: wrong variable name used for resource files
- fix: lazy logging format use %s no f strings
- exclude config test if no config files selected
- jinja template - replace pgk with project

### Refactor

- bump version
- **tasks.py**: remove commented code
- **{{-cookiecutter.pkg_name-}}.py**: escape main() from mypy check
- **post_installation.py**: replace hard coded description text
- **development.in**: remove eradicate as not flake8v6 compatible
- add raise(SystemError(main)) idiom
- **tasks**: remove unused f string
- update pre-commit versions
- correct logger message string
- migrate deprecated importlib.resources functions

## 1.2.1 (2022-08-01)

### Fix

- **__init__.py**: log file path fully relative

### Refactor

- **changelog.md**: remove markdown

## 1.2.0 (2022-08-01)

### Feat

- bump version after new feature
- Add provision for example scripts

### Fix

- **setup.cfg**: error in script entry point

## 1.1.1 (2022-07-21)

### Fix

- **setup.cfg**: entry point for cli script

## 1.1.0 (2022-07-21)

### Fix

- template git branch name
- add config command to readthedocs.yml
- **code**: incorrect markdown

## v1.0.0 (2022-05-06)
