import sys
from typing import Union

import regex
from regexs import regexs_class

regex.cache_all(True)

# https://regex101.com/r/fBLUOp/2 (old)
# re = r"\w{1,}( \*{0,} {0,}\w{1,}(\[[0-9]{0,}\]){0,}){1,} {0,}= {0,}(([0-9]{1,})|(\".*\")|(\{.*\})|([&*]{1,}\w{1,})|(NULL)) {0,};{1}" # noqa: E501
# https://regex101.com/r/ohzzuZ/1 (new)
re = r"\w{1,} {0,}\n{0,}( \*{0,} {0,}\n{0,} {0,}\w{1,} {0,}\n{0,} {0,}(\[ {0,}\n{0,} {0,}[0-9]{0,} {0,}\n{0,} {0,}\]){0,} {0,}\n{0,} {0,}){1,} {0,}= {0,}\n{0,} {0,}(([0-9]{1,})|((\".*\" {0,}\\){0,}(\".*\"){1})|(\{.*\})|([&*]{1,} {0,}\n{0,} {0,}\w{1,})|(NULL)|(\(.{2,}\).*)) {0,}\n{0,} {0,};{1}"  # noqa: E501
reg = regex.compile(re)


def match(text: str, timeout=1) -> Union[None, regexs_class.RegexsResult]:
    try:
        res = reg.match(text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:match: {esc}: {text}", file=sys.stderr)
        return None
    return regexs_class.RegexsResult(text, res.start(), res.end())


def sub(text: str, replace: str, timeout=1) -> None:
    try:
        return reg.sub(replace, text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:sub: {esc}: {text}", file=sys.stderr)
