from rich.console import Console

from normatrix.config.config_class import Config
from normatrix.config.from_cmdline import from_cmdline
from normatrix.config.from_json import from_json


def get_config(console: Console) -> Config:
    conf = Config(console)
    conf_cmdline = from_cmdline(console)
    conf = conf + conf_cmdline
    conf_json = from_json(console)
    conf = conf + conf_json
    return conf
