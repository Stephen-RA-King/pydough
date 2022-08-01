"""Top-level package for {{ cookiecutter.pkg_name }}."""

{%- if cookiecutter.use_logging == 'y' %}
import logging.config
{% endif %}
from importlib import resources
{%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
import json{% endif %}
{%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
import configparser{% endif %}
{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
import toml  # type: ignore{% endif %}
{%- if cookiecutter.use_logging == 'y' or cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
import yaml  # type: ignore{% endif %}

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
_yaml_text = resources.read_text("{{ cookiecutter.pkg_name }}", "config.yaml")
yaml_config = yaml.safe_load(_yaml_text)
{% endif -%}

{%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
_json_text = resources.read_text("{{ cookiecutter.pkg_name }}", "config.json")
json_config = json.loads(_json_text)
{% endif -%}

{%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
_ini_text = resources.read_text("{{ cookiecutter.pkg_name }}", "config.ini")
_ini = configparser.ConfigParser()
_ini.optionxform = str  # type: ignore
_ini.read_string(_ini_text)
ini_config = {section: dict(_ini.items(section)) for section in _ini.sections()}
{% endif -%}

{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
_toml_text = resources.read_text("{{ cookiecutter.pkg_name }}", "config.toml")
toml_config = toml.loads(_toml_text)
{% endif %}

__title__ = "{{ cookiecutter.project_name }}"
__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__description__ = "{{ cookiecutter.project_short_description }}"
__email__ = "{{ cookiecutter.email }}"
__license__ = "{{ cookiecutter.license }}"
__copyright__ = "Copyright {% now 'local', '%Y' %} {{ cookiecutter.author_name }}"
