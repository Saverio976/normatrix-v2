from typing import List

from normatrix.config.config_class import Config
from normatrix.errors.norm import _TemplateNormError


class MakeFile:
    def __init__(self, filepath: str, config: Config):
        self.filepath = filepath

    def init(self, config: Config):
        pass

    def check_norm(self, config: Config) -> List[_TemplateNormError]:
        return []
