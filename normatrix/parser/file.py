from typing import List

from normatrix.config.config_class import Config
from normatrix.errors.norm import BadFileExtension, _TemplateNormError
from normatrix.parser.cfile import CFile
from normatrix.parser.makefile import MakeFile


class DefaultFile:
    def __init__(self, filepath: str, config: Config) -> None:
        self.filepath = filepath

    def init(self, config: Config):
        pass

    def check_norm(self, config: Config) -> List[_TemplateNormError]:
        return [BadFileExtension(self.filepath)]


class File:
    def __init__(self, filepath: str, config: Config):
        self.file_obj = DefaultFile(filepath, config)
        if filepath.endswith((".c", ".h")):
            self.file_obj = CFile(filepath, config)
        elif filepath.endswith("Makefile"):
            self.file_obj = MakeFile(filepath, config)

    def init(self, config: Config):
        self.file_obj.init(config)

    def check_norm(self, config: Config) -> List[_TemplateNormError]:
        return self.file_obj.check_norm(config)
