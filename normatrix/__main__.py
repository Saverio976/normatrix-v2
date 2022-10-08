import sys
from typing import List

from normatrix.config.config import get_config
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser import file, get_files
from normatrix.tests.main import main as main_test

config = get_config()

if config.show_config:
    print(f"INFO: config = {config}")

if config.pass_test:
    ex = main_test()
    sys.exit(ex)

for folder in config.paths:
    list_err: List[List[_TemplateNormError]] = []
    files_to_check = get_files.get_all_files(folder, [], [])
    print(files_to_check)
    for filepath in files_to_check:
        print(filepath)
        f = file.File(filepath)
        # try:
        f.init()
        list_err.append(f.check_norm())
        # except Exception as esc:
        #     print(f"ERROR: {esc}", file=sys.stderr)
        print("\n".join([str(x) for x in list_err[-1]]))
        print()
