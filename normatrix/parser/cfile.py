import os
from enum import Enum
from typing import List, Union

from normatrix.errors.norm import _TemplateNormError
from normatrix.regexs import r_declaration  # 2
from normatrix.regexs import r_for  # 7
from normatrix.regexs import r_function  # 9
from normatrix.regexs import r_if  # 6
from normatrix.regexs import r_macro  # 1
from normatrix.regexs import r_prototype  # 3
from normatrix.regexs import r_struct  # 4
from normatrix.regexs import r_union  # 5
from normatrix.regexs import r_while  # 8
from normatrix.regexs.regexs_class import RegexsResult


class CContextType(Enum):
    DECLARATION = "variable declaration"
    FOR = "for loop"
    FUNCTION = "function implementation"
    IF = "if statement"
    MACRO = "macro definition"
    PROTOTYPE = "function prototype"
    STRUCT = "struct definition"
    UNION = "union definition"
    WHILE = "while loop"


order_parsers = [
    (r_macro, CContextType.MACRO),
    (r_declaration, CContextType.DECLARATION),
    (r_prototype, CContextType.PROTOTYPE),
    (r_struct, CContextType.STRUCT),
    (r_union, CContextType.UNION),
    (r_if, CContextType.IF),
    (r_for, CContextType.FOR),
    (r_while, CContextType.WHILE),
    (r_function, CContextType.FUNCTION),
]


def find_ccontext(stack: List[str]) -> Union[None, "CContext"]:
    joined = "\n".join(stack)
    for mod, _type in order_parsers:
        match = mod.match(joined)
        if not match:
            continue
        index_newline = None if "\n" not in joined else joined.index("\n")
        if not index_newline or match.start >= index_newline:
            continue
        nb_line = joined.count("\n", match.start, match.end)
        context = CContext(_type, match, nb_line)
        return context
    return None


def parse_text_lines(text: List[str]) -> Union[None, List["CContext"]]:
    stack = []
    res = []

    for i, line in enumerate(text):
        stack.append(line)
        matching = find_ccontext(stack)
        if not matching:
            continue
        res.append(matching)
    return res


class CContext:
    def __init__(
        self, type: CContextType, matching: RegexsResult, nb_line: int
    ) -> None:
        self.type = type
        self.matching = matching
        self.nb_lines = nb_line
        self.childs: List["CContext"] = []
        parsed = parse_text_lines(matching.matching.split("\n"))
        if parsed:
            self.childs = parsed

    def __str__(self):
        ret = f"---> {self.type}:{self.nb_lines}\n"
        ret += f"{self.matching}"
        if not str(self.matching).endswith("\n"):
            ret += "\n"
        ret += f"- nb childs: {len(self.childs)}\n"
        return ret


class CFile:
    def __init__(self, filepath: str) -> None:
        if not os.path.isfile(filepath):
            raise os.error(f"Invalid filepath: {filepath}")
        self.filepath = filepath
        self.lines_origin: List[str] = []
        self.text_origin = ""
        self.parsed_context: List[CContext] = []
        self.is_init = False

    def init(self):
        with open(self.filepath) as f:
            self.lines_origin = f.readlines()
        self.text_origin = "\n".join(self.lines_origin)
        if not self.lines_origin:
            return False
        parsed = parse_text_lines(self.lines_origin)
        if parsed:
            self.parsed_context = parsed
        self.is_init = True
        print(self)

    def check_norm(self) -> List[_TemplateNormError]:
        return []

    def __str__(self):
        ret = f"file: {self.filepath}\n"
        for i, ctx in enumerate(self.parsed_context):
            ret += f"ctx n{i}:\n"
            ret += str(ctx)
        return ret
