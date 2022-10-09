from typing import List

from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.makefile import MakeFile


def check(file: MakeFile) -> List[_TemplateNormError]:
    return []
