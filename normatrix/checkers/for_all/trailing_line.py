from typing import List

from normatrix.errors.norm import LeadingTrailingLine, _TemplateNormError
from normatrix.parser._file import _File


def check(file: _File) -> List[_TemplateNormError]:
    if not file.text_origin:
        return []
    if file.text_origin.endswith("\n\n"):
        return [
            LeadingTrailingLine(
                file.filepath,
                file.text_origin.count("\n"),
                "No 2 empty line at end of file",
            )
        ]
    if not file.text_origin.endswith("\n"):
        return [
            LeadingTrailingLine(
                file.filepath,
                file.text_origin.count("\n"),
                "End of file must be with a \\n",
            )
        ]
    return []
