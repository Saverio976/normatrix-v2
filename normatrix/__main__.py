import sys
from typing import List

from rich.console import Console

from normatrix.config.config import get_config
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser import file, get_files
from normatrix.tests.main import main as main_test

config = get_config(Console(record=True))

config.console.rule("[bold blue]normatrix", style="bold blue")
config.console.print("Check the Epitech C Coding Style", style="italic")
config.console.line(2)

if config.show_config:
    config.console.rule("Parsed Config from cmdline + `.normatrix.json`", style="blue")
    config.console.print_json(data=config)
    config.console.line()

if config.pass_test:
    config.console.rule("Execute Tests", style="blue")
    ex = main_test()
    config.console.line()
    sys.exit(ex)


config.console.rule("Norm:", style="blue")
for folder in config.paths:
    list_all_err: List[List[_TemplateNormError]] = []
    try:
        files_to_check = get_files.get_all_files(folder, [], [])
    except Exception:
        config.console.print(":warning: [red]An Error Occured")
        config.console.print_exception()
        continue
    for filepath in files_to_check:
        list_err: List[_TemplateNormError] = []
        config.console.print(f"[{filepath}]({filepath})")
        try:
            f = file.File(filepath, config)
            f.init(config)
            list_err = f.check_norm(config)
            list_all_err.append(list_err)
        except Exception:
            config.console.print(":warning: [red]An Error Occured")
            config.console.print_exception()
        else:
            config.console.print("\n".join([str(x) for x in list_err]))
        config.console.line()
