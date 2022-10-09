from typing import List

from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.file import DefaultFile


def check(file: DefaultFile) -> List[_TemplateNormError]:
    return []
