from normatrix.config.config_class import Config
from normatrix.parser._file import _File


class MakeFile(_File):
    def __init__(self, filepath: str, config: Config):
        super().__init__(filepath, config)

    def init(self, config: Config):
        self.is_init = True
