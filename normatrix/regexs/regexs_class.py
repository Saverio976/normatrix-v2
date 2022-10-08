class RegexsResult:
    def __init__(self, text: str, start: int, end: int) -> None:
        if len(text) <= end:
            raise ValueError(
                f"{__file__}: ERROR: end of matching is out of range ({end})"
            )
        if len(text) <= start:
            raise ValueError(
                f"{__file__}: ERROR: start of matching is out of range ({start})"  # noqa: E501
            )
        if end < 0:
            raise ValueError(
                f"{__file__}: ERROR: end of matching is out of range ({end})"
            )
        if start < 0:
            raise ValueError(
                f"{__file__}: ERROR: end of matching is out of range ({start})"
            )
        self.text = text
        self.start = start
        self.end = end
        self.matching = text[start : (end + 1)]
