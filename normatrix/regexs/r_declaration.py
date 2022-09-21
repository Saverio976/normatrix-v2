import sys

import regex

# https://regex101.com/r/fBLUOp/1
re = r"\w{1,}( \*{0,} {0,}\w{1,}(\[[0-9]{0,}\]){0,}){1,} "
r"{0,}= {0,}(([0-9]{1,})|(\".*\")|(\{.*\})|([&*]{1,}\w{1,})|(NULL)) {0,};{0,}"
reg = regex.compile(re)


def match(text: str, timeout=1):
    try:
        return reg.match(text, timeout=timeout)
    except TimeoutError as esc:
        sys.stderr.write(f"ERROR: {__file__}:match: {esc}: {text}")
        return None


def sub(text: str, replace: str, timeout=1):
    try:
        return reg.sub(replace, text, timeout=timeout)
    except TimeoutError as esc:
        sys.stderr.write(f"ERROR: {__file__}:sub: {esc}: {text}")
        return None


def search(text: str, timeout=1):
    try:
        return reg.search(text, timeout=timeout)
    except TimeoutError as esc:
        sys.stderr.write(f"ERROR: {__file__}:search: {esc}: {text}")
        return None
