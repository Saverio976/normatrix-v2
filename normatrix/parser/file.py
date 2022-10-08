from typing import List

from normatrix.errors.norm import BadFileExtension, _TemplateNormError
from normatrix.parser.cfile import CFile
from normatrix.parser.makefile import MakeFile


class DefaultFile:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def init(self):
        pass

    def check_norm(self) -> List[_TemplateNormError]:
        return [BadFileExtension(self.filepath)]


class File:
    def __init__(self, filepath: str):
        self.file_obj = DefaultFile(filepath)
        if filepath.endswith((".c", ".h")):
            self.file_obj = CFile(filepath)
        elif filepath.endswith("Makefile"):
            self.file_obj = MakeFile(filepath)

    def init(self):
        self.file_obj.init()

    def check_norm(self) -> List[_TemplateNormError]:
        return self.file_obj.check_norm()
