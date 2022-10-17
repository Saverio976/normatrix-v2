from typing import List

from normatrix.config.config_class import Config
from normatrix.errors.norm import BadFileExtension, _TemplateNormError
from normatrix.parser._file import _File
from normatrix.parser.cfile import CFile
from normatrix.parser.makefile import MakeFile


class DefaultFile(_File):
    def __init__(self, filepath: str, config: Config) -> None:
        super().__init__(filepath, config)

    def init(self):
        self.is_init = True

    def check_norm(self) -> List[_TemplateNormError]:
        return [BadFileExtension(self.filepath)]


class File:
    def __init__(self, filepath: str, config: Config):
        self.file_obj: _File
        if filepath.endswith((".c", ".h")):
            self.file_obj = CFile(filepath, config)
        elif filepath.endswith("Makefile"):
            self.file_obj = MakeFile(filepath, config)
        else:
            self.file_obj = DefaultFile(filepath, config)

    def init(self):
        self.file_obj.init()

    def check_norm(self) -> List[_TemplateNormError]:
        return self.file_obj.check_norm()
