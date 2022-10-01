import sys

import regex
from regexs import regexs_class

regex.cache_all(True)

# https://regex101.com/r/fBLUOp/2
re = r"\w{1,}( \*{0,} {0,}\w{1,}(\[[0-9]{0,}\]){0,}){1,} "
r"{0,}= {0,}(([0-9]{1,})|(\".*\")|(\{.*\})|([&*]{1,}\w{1,})|(NULL)) {0,};{1}"
reg = regex.compile(re)


def match(text: str, timeout=1):
    try:
        res = reg.match(text, timeout=timeout)
    except TimeoutError as esc:
        sys.stderr.write(f"ERROR: {__file__}:match: {esc}: {text}")
        return None
    return regexs_class.RegexsResult(text, res.start(), res.end())


def sub(text: str, replace: str, timeout=1) -> None:
    try:
        return reg.sub(replace, text, timeout=timeout)
    except TimeoutError as esc:
        sys.stderr.write(f"ERROR: {__file__}:sub: {esc}: {text}")
