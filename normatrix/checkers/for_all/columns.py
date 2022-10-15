from typing import List

from normatrix.errors.norm import ColumnsNumber, _TemplateNormError
from normatrix.parser._file import _File


def check_nbcol(file: _File) -> List[_TemplateNormError]:
    if not file.text_origin:
        return []
    errs = []
    for i, line in enumerate(file.lines_origin):
        txt = line.expandtabs(4)
        if len(txt) >= 80:
            errs.append(ColumnsNumber(file.filepath, i + 1, "too many columns"))
    return errs
