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
from importlib.metadata import version

# Third party modules
{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
import toml  # type: ignore{% endif %}
{%- if cookiecutter.use_logging == 'y' or cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
import yaml  # type: ignore{% endif %}

__version__ = version("{{ cookiecutter.pkg_name }}")

{% if cookiecutter.use_logging == 'y' -%}
LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.handlers.RotatingFileHandler
    level: DEBUG
    filename: logs/log.txt
    maxBytes: 1048576    # 1MB
    backupCount: 3       # keeps log.txt, log.txt.1, log.txt.2, log.txt.3
    formatter: timestamp
    encoding: utf-8

formatters:
  basic:
    style: "{"
    format: "{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {filename}:{lineno} - {message}"

loggers:
  init:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("init")
{%- endif %}

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
    pickle_content = pickle.loads(_pickle_bytes)
{% endif %}
