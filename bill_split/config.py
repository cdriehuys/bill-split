from pathlib import Path

import yaml


CONFIG_LOCATION = Path.home() / ".bill-split.yml"


def read_config_file() -> dict:
    """
    Read the contents of the config file and return the raw data it
    contains.

    Returns:
        The contents of the config file as a dictionary.
    """
    return yaml.safe_load(open(CONFIG_LOCATION))
