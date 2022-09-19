import json
import sys
from argparse import Namespace
from typing import Any, Union


class __OutputFormat:
    __choices = {
        "HTML": "html",
        "MARKDOWN": "md",
        "TERM_COLOR": "term_color",
        "TERM_RICH": "term_rich",
    }

    def __init__(self, any: Any = None) -> None:
        self._name_ = None
        self._value_: Union[None, str] = None
        self.__is_defined = False
        if any is None:
            raise ValueError("Can't create OutputFormat from nothing")
        if str(any) in self.__choices.keys():
            self._name_ = str(any)
            self._value_ = self.__choices[str(any)]
            self.__is_defined = True
        elif str(any) in self.__choices.values():
            for key, value in self.__choices.items():
                if str(any) == value:
                    self._name_ = key
                    self._value_ = value
                    self.__is_defined = True
                    break
        if self.__is_defined is False:
            raise ValueError(f"OutputFormat can't be created from {any})")
        self.__iterrable = list(self.__choices.keys())

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__iterrable):
            raise StopIteration
        result = self.__iterrable[self.__index]
        self.__index += 1
        return result

    def __eq__(self, __o: object) -> bool:
        if OutputFormat(__o) is None:
            return False
        if str(self) == str(OutputFormat(__o)):
            return True
        if self._name_ == OutputFormat(__o)._name_:
            return True
        return False

    def __contains__(self, obj: object) -> bool:
        for elem in self:
            if elem == obj:
                return True
        return False

    def __str__(self):
        return self._value_

    @staticmethod
    def to_list():
        allobj = list(OutputFormat.__choices.keys()) + list(
            OutputFormat.__choices.values()
        )
        return allobj


class OutputFormat(__OutputFormat):
    def __new__(cls, any: Any = None) -> Union["OutputFormat", None]:
        try:
            obj = object.__new__(cls)
            super().__init__(obj, any)
        except ValueError:
            return None
        return obj


class __Defaults:
    operators_plugin = True
    preview = False
    only_error = False
    no_fclean = False
    link_line = False
    format = OutputFormat("TERM_RICH")
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
