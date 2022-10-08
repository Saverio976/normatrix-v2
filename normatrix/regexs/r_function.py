import sys
from typing import Union

import regex
from regexs import regexs_class

regex.cache_all(True)

# https://regex101.com/r/F6p3r9/2
re = r"\w{1,}( \*{0,} {0,}\w{1,}(\[[0-9]{0,}\]){0,}){1,} {0,}"
r"\((\w{1,}( \*{0,} {0,}\w{1,}(\[[0-9]{0,}\]){0,}){1,} {0,},{0,1} {0,}){0,}\)"
r" {0,}\n{0,}\{"
reg = regex.compile(re)


def is_token_not_escaped(text: str, index: int) -> bool:
    if index < 0 or len(text) <= index:
        return False
    if index - 1 == 0:
        return True
    if text[index - 1] != "\\":
        return True
    if index - 2 == 0:
        return False
    if text[index - 2] == "\\":
        return True
    return False


def match(text: str, timeout=1) -> Union[None, regexs_class.RegexsResult]:
    try:
        res = reg.match(text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:match: {esc}: {text}", file=sys.stderr)
        return None
    if res is None:
        return None
    start = res.start()
    end = res.end()
    fifo = ["{"]
    while len(fifo) > 0 and len(text) > end + 1:
        end += 1
        if text[end] == "}" and is_token_not_escaped(text, end):
            fifo.pop(-1)
        elif text[end] == "{" and is_token_not_escaped(text, end):
            fifo.append("{")
    return regexs_class.RegexsResult(text, start, end + 1)


def sub(text: str, replace: str, timeout=1) -> None:
    is_ok = True
    while is_ok:
        patr = match(text, timeout=timeout)
        if patr:
            text = text.replace(patr.matching, replace)
        else:
            is_ok = False
