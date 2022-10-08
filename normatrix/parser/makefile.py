from typing import List

from normatrix.errors.norm import _TemplateNormError


class MakeFile:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def init(self):
        pass

    def check_norm(self) -> List[_TemplateNormError]:
        return []
