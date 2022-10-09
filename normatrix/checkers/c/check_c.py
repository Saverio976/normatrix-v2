from typing import List

from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.cfile import CFile


def check(file: CFile) -> List[_TemplateNormError]:
    return []
