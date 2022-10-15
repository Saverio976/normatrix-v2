from typing import List

from normatrix.checkers.c.comma import check_comma
from normatrix.checkers.c.nb_function_per_file import check_nfpf
from normatrix.checkers.c.tabulation import check_tab
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.cfile import CFile

checkerss = [check_nfpf, check_tab, check_comma]


def check(file: CFile) -> List[_TemplateNormError]:
    err = []
    for check in checkerss:
        cur_err = check(file)
        err.extend(cur_err)
    return err
