from typing import List

# checkers for c
from normatrix.checkers.c.nb_function_per_file import check_nfpf
from normatrix.checkers.c.tabulation import check_tab
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.cfile import CFile

# end checkers for c


checkerss = [check_nfpf, check_tab]


def check(file: CFile) -> List[_TemplateNormError]:
    err = []
    for check in checkerss:
        cur_err = check(file)
        err.extend(cur_err)
    return err
