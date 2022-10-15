from typing import List

from normatrix.checkers.for_all.columns import check_nbcol
from normatrix.checkers.for_all.leading_line import check_line_start
from normatrix.checkers.for_all.trailing_line import check_line_end
from normatrix.checkers.for_all.trailing_space import check_space
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser._file import _File

checkerss = [
    check_line_start,
    check_space,
    check_line_end,
    check_nbcol,
]


def check(file: _File) -> List[_TemplateNormError]:
    errs: List[_TemplateNormError] = []
    for checker in checkerss:
        errs.extend(checker(file))
    return errs
