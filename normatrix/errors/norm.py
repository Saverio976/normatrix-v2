from enum import Enum


class Severity(Enum):
    MAJOR = "major"
    MINOR = "minor"
    INFO = "info"


class _TemplateNormError:
    def __init__(
        self,
        filepath: str,
        line: int,
        severity: Severity,
        rule: str,
        explanation: str,
        msg: str = "",
    ):
        self.filepath = filepath
        self.line = line
        self.msg = msg
        self.rule = rule
        self.explanation = explanation
        self.severity = severity

    def __str__(self) -> str:
        ret = f"{self.filepath}:{self.line} :: {self.rule}::"
        ret += f"{self.severity.value}"
        if self.msg:
            ret += f" :: {self.msg}"
        ret += f"\nexplanation: {self.explanation}"
        return ret

    def show(self):
        print(self.__str__())


class BadFileExtension(_TemplateNormError):
    def __init__(self, filepath: str, msg: str = ""):
        super().__init__(
            filepath=filepath,
            line=0,
            severity=Severity.MAJOR,
            rule="C-O1",
            explanation="The repository must not contain compiled temporary or unnecessary files",  # noqa: E501
            msg=msg,
        )


class TooManyFunctions(_TemplateNormError):
    def __init__(self, filepath: str, msg: str):
        super().__init__(
            filepath=filepath,
            line=0,
            severity=Severity.MAJOR,
            rule="C-O3",
            explanation="Beyond 5 functions in your file, you must subdivide your logical entity into several sub-entities",  # noqa: E501
            msg=msg,
        )


class BadFileName(_TemplateNormError):
    def __init__(self, filepath: str, msg: str):
        super().__init__(
            filepath=filepath,
            line=0,
            severity=Severity.MINOR,
            rule="C-O4",
            explanation="All file names and folders must be in English, according to the snake_case convention (that is, only composed of lowercase, numbers, and underscores)",  # noqa: E501
            msg=msg,
        )


class FileHeader(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-G1",
            explanation="C files (.c, .h, . . . ) and every Makefiles must always start with the standard header of the school",  # noqa: E501
            msg=msg,
        )


class SepBetweenFunction(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-G2",
            explanation="Inside a source file, implementations of functions must be separated by one and only one empty line",  # noqa: E501
            msg=msg,
        )


class PreprocessorIndent(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-G3",
            explanation="The preprocessor directives must be indented according to the level of indirection",  # noqa: E501
            msg=msg,
        )


class GlobalVariable(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-G4",
            explanation="Global variables must be avoided as much as possible. Only global constants should be used",  # noqa: E501
            msg=msg,
        )


class IncludeFile(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-G5",
            explanation="include directive must only include C header (.h) files",  # noqa: E501
            msg=msg,
        )


class LineEnding(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-G6",
            explanation="Line endings must be done in UNIX style (with \\n)",
            msg=msg,
        )


class TrailingSpace(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-G7",
            explanation="No trailing spaces must be present at the end of a line",  # noqa: E501
            msg=msg,
        )


class LeadingTrailingLine(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-G7",
            explanation="No leading empty lines must be present. No more than 1 trailing empty line must be present",  # noqa: E501
            msg=msg,
        )


class NamingFunction(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-F2",
            explanation="All function names must be in English, according to the snake_case convention (meaning that it is composed only of lowercase, numbers, and underscores)",  # noqa: E501
            msg=msg,
        )


class ColumnsNumber(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-F3",
            explanation="The length of a line must not exceed 80 columns (not to be confused with 80 characters)",  # noqa: E501
            msg=msg,
        )


class FunctionLineNumber(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-F4",
            explanation="The body of a function should be as short as possible, and must not exceed 20 lines",  # noqa: E501
            msg=msg,
        )


class FunctionParametersNumber(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-F5",
            explanation="A function must not have more than 4 parameters",
            msg=msg,
        )


class FunctionWithoutParameter(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-F6",
            explanation="A function taking no parameters must take void as a parameter in the function declaration",  # noqa: E501
            msg=msg,
        )


class StructureParameter(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-F7",
            explanation="Structures must be transmitted as arguments using a pointer, not by copy",  # noqa: E501
            msg=msg,
        )


class CommentInFunction(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-F8",
            explanation="There must be no comment within a function",
            msg=msg,
        )


class NestedFunction(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-F9",
            explanation="Nested functions are not allowed",
            msg=msg,
        )


class ManyStatementOnLine(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-L1",
            explanation="A line must correspond to only one statement",
            msg=msg,
        )


class BadIndentation(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-L2",
            explanation="Each indentation level must be done by using 4 spaces. No tabulations may be used for indentation",  # noqa: E501
            msg=msg,
        )


class BadSpace(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-L3",
            explanation="When using a space as a separator, one and only one space character must be used. Always place a space after a comma or a keyword (if it has arguments). there must be no spaces between the name of a function and the opening parenthesis, after a unary operator, or before a semicolon. In the precise case of a for control structure, if a semicolon inside the parentheses is not immediately followed by another semicolon, it must be followed by a space. All binary and ternary operators must be separated from their arguments by a space on both sides",  # noqa: E501
            msg=msg,
        )


class BadCurlyBracket(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-L4",
            explanation="Opening curly brackets must be at the end of the line, after the content it precedes, except for functions definitions where they must be placed alone on their line. Closing curly brackets must be alone on their line, except in the case of else/else if control structures, enum declarations, or structure declarations (with or without an associated typedef)",  # noqa: E501
            msg=msg,
        )


class MissPlacedVariableDeclaration(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-L5",
            explanation="Variables must be declared at the beginning of the scope of the function, Only one variable must be declared per line. The for control structures may also optionally declare variables in their initialization part",  # noqa: E501
            msg=msg,
        )


class BadLineJumps(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-L6",
            explanation="A line break must separate the variable declarations from the remainder of the function. No other line breaks must be present in the scope of a function",  # noqa: E501
            msg=msg,
        )


class BadNamingIdentifiers(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-V1",
            explanation="All identifier names must be in English, according to the snake_case convention (meaning it is composed exclusively of lowercase, numbers, and underscores). The type names defined with typedef must end with _t. The names of macros and global constants and the content of enums must be written in UPPER_SNAKE_CASE",  # noqa: E501
            msg=msg,
        )


class MissPlacedPointer(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MINOR,
            rule="C-V3",
            explanation="The pointer symbol (*) must be attached to the associated variable, with no spaces",  # noqa: E501
            msg=msg,
        )


class TooManyConditionBranch(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-C1",
            explanation="A conditionnal block (while, for, if, else, . . . ) must not contain more than 3 branches",  # noqa: E501
            msg=msg,
        )


class NoGoto(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-C3",
            explanation="Using the goto keyword is forbidden",
            msg=msg,
        )


class FunctionInHeader(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-H1",
            explanation="non static inline function are banned from header file",  # noqa: E501
            msg=msg,
        )


class NoIncludeGuard(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-H2",
            explanation="Headers must be protected from double inclusion",
            msg=msg,
        )


class MacroOnMultiLine(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.MAJOR,
            rule="C-H3",
            explanation="Macros must match only one statement, and fit on a single line",  # noqa: E501
            msg=msg,
        )


class BadEndLineBreak(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.INFO,
            rule="C-A3",
            explanation="Files must end with a line break",
            msg=msg,
        )


class Info(_TemplateNormError):
    def __init__(self, filepath: str, line: int, msg: str):
        super().__init__(
            filepath=filepath,
            line=line,
            severity=Severity.INFO,
            rule="info",
            explanation="tip of the dev",
        )
