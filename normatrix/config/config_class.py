from argparse import Namespace
from enum import Enum
from typing import Any


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
    options = [
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


class Config:
    operators_plugin = __Defaults.operators_plugin
    preview = __Defaults.preview
    only_error = __Defaults.only_error
    no_fclean = __Defaults.no_fclean
    link_line = __Defaults.link_line
    format = __Defaults.format
    paths = __Defaults.paths
    libc_banned_func = __Defaults.libc_banned_func
    file_extension_banned = __Defaults.file_extension_banned

    def __init__(self) -> None:
        pass

    def __add_one(
        self, other: "Config" | Namespace, attr: str, newConf: "Config"
    ) -> Any:
        if getattr(self, attr, None) is None and getattr(other, attr, None) is not None:
            setattr(newConf, attr, getattr(other, attr))
            return getattr(other, attr)
        if getattr(self, attr) != getattr(__Defaults(), attr):
            setattr(newConf, attr, getattr(self, attr))
            return getattr(self, attr)
        if getattr(other, attr, None) is None:
            setattr(newConf, attr, getattr(__Defaults(), attr))
            return getattr(__Defaults(), attr)
        setattr(newConf, attr, getattr(other, attr))
        return getattr(other, attr)

    def __add__(self, other):
        conf = Config()
        if not isinstance(other, "Config" | Namespace):
            print(f"{__file__}: ERROR: Could not add {self} and {other}")
            return self
        for attr in __Defaults.options:
            self.__add_one(other, attr, conf)
        return conf
