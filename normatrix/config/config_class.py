import json
import sys
from argparse import Namespace
from enum import Enum
from typing import Any, Union


class OutputFormat(Enum):
    HTML = "html"
    MARKDOWN = "md"
    TERM_COLOR = "term_color"
    TERM_RICH = "term_rich"


class __Defaults:
    operators_plugin = True
    preview = False
    only_error = False
    no_fclean = False
    link_line = False
    format = OutputFormat.TERM_RICH
    paths = ["."]
    libc_banned_func = [
        "printf",
        "memset",
        "strcpy",
        "strcat",
        "calloc",
        "fprintf",
    ]
    file_extension_banned = [
        "*.a",
        "*.o",
        "*.so",
        "*.gch",
        "*~",
        "*#",
        "*.d",
    ]
    _options = [
        "operators_plugin",
        "preview",
        "only_error",
        "no_fclean",
        "link_line",
        "format",
        "paths",
        "libc_banned_func",
        "file_extension_banned",
    ]


class Config(__Defaults):
    def __init__(self) -> None:
        super().__init__()

    def __add_one(
        self, other: Union["Config", Namespace], attr: str, newConf: "Config"
    ) -> Any:
        default = Config()
        if getattr(self, attr, None) is None and getattr(other, attr, None) is not None:
            setattr(newConf, attr, getattr(other, attr))
            return getattr(other, attr)
        if getattr(self, attr) != getattr(default, attr):
            setattr(newConf, attr, getattr(self, attr))
            return getattr(self, attr)
        if getattr(other, attr, None) is None:
            setattr(newConf, attr, getattr(default, attr))
            return getattr(default, attr)
        setattr(newConf, attr, getattr(other, attr))
        return getattr(other, attr)

    def __add__(self, other):
        conf = Config()
        try:
            for attr in self._options:
                self.__add_one(other, attr, conf)
        except Exception as esc:
            print(f"ERROR: Could not add {self} and {other} : {esc}", file=sys.stderr)
        return conf

    def __str__(self):
        dico = {key: str(getattr(self, key)) for key in self._options}
        return json.dumps(dico, ensure_ascii=True, indent=4)
