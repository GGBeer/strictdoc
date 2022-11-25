from typing import List


class GrammarReferenceType:
    PARENT_REQ_REFERENCE = "ParentReqReference"
    FILE_REFERENCE = "FileReference"
    EXTERNAL_REFERENCE = "ExternalReference"


class GrammarElementField:
    def __init__(self):
        self.title: str = ""
        self.type: str = ""
        self.required: bool = False


class GrammarElementFieldString(GrammarElementField):
    def __init__(self, parent, title: str, type: str, required: str):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.type: str = type
        self.required: bool = required == "True"

    def __str__(self):
        return (
            "GrammarElementFieldString("
            f"parent: {self.parent}, "
            f"title: {self.title}, "
            f"type: {self.type}, "
            f"required: {self.required}"
            ")"
        )


class GrammarElementFieldSingleChoice(GrammarElementField):
    def __init__(self, parent, title: str, type: str, options: List[str], required: str):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.type: str = type
        self.options: List[str] = options
        self.required: bool = required == "True"


class GrammarElementFieldMultipleChoice(GrammarElementField):
    def __init__(self, parent, title: str, type: str, options: List[str], required: str):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.type: str = type
        self.options: List[str] = options
        self.required: bool = required == "True"


class GrammarElementFieldTag(GrammarElementField):
    def __init__(self, parent, title: str, type: str, required: str):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.type: str = type
        self.required: bool = required == "True"

    def __str__(self):
        return (
            "GrammarElementFieldTag("
            f"parent: {self.parent}, "
            f"title: {self.title}, "
            f"type: {self.type}, "
            f"required: {self.required}"
            ")"
        )


class GrammarElementFieldTypeValue(GrammarElementField):
    def __init__(self, parent, title: str, type: str, types: List[str], required: str):
        super().__init__()
        self.parent = parent
        self.type: str = type
        self.title: str = title
        self.types: List[str] = types
        self.required: bool = required == "True"

    def __str__(self):
        return (
            "GrammarElementFieldTypeValue("
            f"parent: {self.parent}, "
            f"title: {self.title}, "
            f"type: {self.type}({', '.join(self.types)}), "
            f"required: {self.required}"
            ")"
        )

    def _print_grammar_field_type(self):
        return (
            f"  - TITLE: {self.title}\n"
            f"    TYPE: {self.type}({', '.join(self.types)})\n"
            f"    REQUIRED: {self.required!s}\n"
        )
