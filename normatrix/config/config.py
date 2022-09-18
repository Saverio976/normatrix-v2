from normatrix.config.config_class import Config
from normatrix.config.from_cmdline import from_cmdline
from normatrix.config.from_json import from_json


def get_config() -> Config:
    conf = Config()
    conf_cmdline = from_cmdline()
    conf = conf + conf_cmdline
    conf_json = from_json()
    conf = conf + conf_json
    return conf
