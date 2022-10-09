from typing import List

from normatrix.checkers.c import check_c
from normatrix.checkers.default import check_default
from normatrix.checkers.makefile import check_makefile
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.cfile import CFile
from normatrix.parser.file import DefaultFile, File
from normatrix.parser.makefile import MakeFile

choices = {
    CFile: check_c.check,
    DefaultFile: check_default.check,
    MakeFile: check_makefile.check,
}


def check(file: File) -> List[_TemplateNormError]:
    for _type, func in choices.items():
        if isinstance(file.file_obj, _type):
            return func(file.file_obj)
    return []
