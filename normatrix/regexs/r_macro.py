import sys
from typing import Union

import regex
from regexs import regexs_class

# https://regex101.com/r/tp3bAf/1
re = r"#define \w{1,}(\((\w,{0,} {0,}){0,}\)){0,1} {0,}(.*\\\n){0,}(.*){1}"
reg = regex.compile(re)


def match(text: str, timeout=1) -> Union[None, regexs_class.RegexsResult]:
    try:
        res = reg.match(text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:match: {esc}: {text}", file=sys.stderr)
        return None
    if not res:
        return None
    return regexs_class.RegexsResult(text, res.start(), res.end())


def sub(text: str, replace: str, timeout=1) -> None:
    try:
        reg.sub(replace, text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:sub: {esc}: {text}", file=sys.stderr)
