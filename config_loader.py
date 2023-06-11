import os
import pathlib


def read_config_file(section, key):
    from configparser import ConfigParser

    config_path = str(pathlib.Path(__file__).parent.absolute()) + '/config.ini'

    config = ConfigParser()
    config.read(config_path)

    value = config.get(section, key)

    if value.lower() == 'true':
        value = True
    elif value.lower() == 'false':
        value = False

    return value


def read_config_from_current_env(key):
    section = os.getenv('env').lower()
    return read_config_file(section, key)
