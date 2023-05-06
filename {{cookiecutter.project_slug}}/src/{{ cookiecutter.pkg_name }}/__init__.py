#!/usr/bin/env python3
"""Top-level package for {{ cookiecutter.pkg_name }}."""
# Core Library modules
{%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
import configparser{% endif %}
{%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
import json{% endif %}
{%- if cookiecutter.use_logging == 'y' %}
import logging.config{% endif %}
{%- if cookiecutter.resource_file == 'pickle' or cookiecutter.resource_file == 'all' %}
import pickle{% endif %}
{%- if cookiecutter.config_file != 'none' or cookiecutter.resource_file != 'none' %}
from importlib.resources import files, as_file{% endif %}

# Third party modules
{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
import toml  # type: ignore{% endif %}
{%- if cookiecutter.use_logging == 'y' or cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
import yaml  # type: ignore{% endif %}

__title__ = "{{ cookiecutter.project_name }}"
__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__description__ = "{{ cookiecutter.project_short_description }}"
__email__ = "{{ cookiecutter.email }}"
__license__ = "{{ cookiecutter.license }}"
__copyright__ = "Copyright {% now 'local', '%Y' %} {{ cookiecutter.author_name }}"


{% if cookiecutter.use_logging == 'y' %}
LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.FileHandler
    level: DEBUG
    filename: {{ cookiecutter.pkg_name }}.log
    encoding: utf-8
    formatter: timestamp

formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {name} - {message}"

loggers:
  init:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("init")
{% endif -%}

{%- if cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
source_yaml = files("{{ cookiecutter.pkg_name }}.resources").joinpath('config.yaml')
with as_file(source_yaml) as _yaml_path:
    _yaml_text = _yaml_path.read_text()
    yaml_config = yaml.safe_load(_yaml_text)
{% endif -%}

{%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
source_json = files("{{ cookiecutter.pkg_name }}.resources").joinpath('config.json')
with as_file(source_json) as _json_path:
    _json_text = _json_path.read_text()
    json_config = json.loads(_json_text)
{% endif -%}

{%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
source_ini = files("{{ cookiecutter.pkg_name }}.resources").joinpath('config.ini')
with as_file(source_ini) as _ini_path:
    _ini_text = _ini_path.read_text()
    _ini = configparser.ConfigParser()
    _ini.optionxform = str  # type: ignore
    _ini.read_string(_ini_text)
    ini_config = {section: dict(_ini.items(section)) for section in _ini.sections()}
{% endif -%}

{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
source_toml = files("{{ cookiecutter.pkg_name }}.resources").joinpath('config.toml')
with as_file(source_toml) as _toml_path:
    _toml_text = _toml_path.read_text()
    toml_config = toml.loads(_toml_text)
{% endif %}

{%- if cookiecutter.resource_file == 'pickle' or cookiecutter.resource_file == 'all' %}
source_pickle = files("{{ cookiecutter.pkg_name }}.resources").joinpath("resource.pickle")
with as_file(source_pickle) as _pickle_file:
    _pickle_bytes = _pickle_file.read_bytes()
    project_content = pickle.loads(_pickle_bytes)
{% endif %}
