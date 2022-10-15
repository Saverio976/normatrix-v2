import sys
from typing import Optional

import regex
from regexs import regexs_class

# https://regex101.com/r/6cB6Ls/1
re = r".*?(?<!\\)"
reg = regex.compile(re)


def search(text: str, timeout=1) -> Optional[regexs_class.RegexsResult]:
    try:
        res = reg.search(text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:search: {esc}: {text}", file=sys.stderr)
        return None
    if not res:
        return None
    return regexs_class.RegexsResult(text, res.start(), res.end(), add_extra=False)


def sub(text: str, replace: str, timeout=1) -> Optional[str]:
    try:
        return reg.sub(replace, text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:sub: {esc}: {text}", file=sys.stderr)
