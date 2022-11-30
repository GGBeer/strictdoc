from typing import List


class RequirementFieldName:
    UID = "UID"
    LEVEL = "LEVEL"
    STATUS = "STATUS"
    TAGS = "TAGS"
    REFS = "REFS"
    TITLE = "TITLE"
    STATEMENT = "STATEMENT"
    RATIONALE = "RATIONALE"
    COMMENT = "COMMENT"


RESERVED_NON_META_FIELDS = [
    RequirementFieldName.REFS,
    RequirementFieldName.TITLE,
    RequirementFieldName.STATEMENT,
    RequirementFieldName.COMMENT,
    RequirementFieldName.RATIONALE,
    RequirementFieldName.LEVEL,
]


class RequirementFieldType:
    STRING = "String"
    SINGLE_CHOICE = "SingleChoice"
    MULTIPLE_CHOICE = "MultipleChoice"
    TAG = "Tag"
    TYPE_VALUE = "TypeValue"


class GrammarReferenceType:
    PARENT_REQ_REFERENCE = "ParentReqReference"
    FILE_REFERENCE = "FileReference"
    EXTERNAL_REFERENCE = "ExternalReference"


class ReferenceType:
    PARENT = "Parent"
    FILE = "File"
    EXTERNAL = "External"

    GRAMMAR_REFERENCE_TYPE_MAP = {
        PARENT: GrammarReferenceType.PARENT_REQ_REFERENCE,
        FILE: GrammarReferenceType.FILE_REFERENCE,
        EXTERNAL: GrammarReferenceType.EXTERNAL_REFERENCE,
    }


class GrammarElementField:
    def __init__(self):
        self.title: str = ""
        self.gef_type: str = ""
        self.required: bool = False


class GrammarElementFieldString(GrammarElementField):
    def __init__(self, parent, title: str, gef_type: str, required: str):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.gef_type: str = gef_type
        self.required: bool = required == "True"

    def __str__(self):
        return (
            "GrammarElementFieldString("
            f"parent: {self.parent}, "
            f"title: {self.title}, "
            f"gef_type: {self.gef_type}, "
            f"required: {self.required}"
            ")"
        )


class GrammarElementFieldSingleChoice(GrammarElementField):
    def __init__(  # pylint: disable=too-many-arguments
        self,
        parent,
        title: str,
        gef_type: str,
        options: List[str],
        required: str,
    ):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.gef_type: str = gef_type
        self.options: List[str] = options
        self.required: bool = required == "True"


class GrammarElementFieldMultipleChoice(GrammarElementField):
    def __init__(  # pylint: disable=too-many-arguments
        self,
        parent,
        title: str,
        gef_type: str,
        options: List[str],
        required: str,
    ):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.gef_type: str = gef_type
        self.options: List[str] = options
        self.required: bool = required == "True"


class GrammarElementFieldTag(GrammarElementField):
    def __init__(self, parent, title: str, gef_type: str, required: str):
        super().__init__()
        self.parent = parent
        self.title: str = title
        self.gef_type: str = gef_type
        self.required: bool = required == "True"

    def __str__(self):
        return (
            "GrammarElementFieldTag("
            f"parent: {self.parent}, "
            f"title: {self.title}, "
            f"gef_type: {self.gef_type}, "
            f"required: {self.required}"
            ")"
        )


class GrammarElementFieldTypeValue(
    GrammarElementField
):  # pylint: disable=too-many-arguments
    def __init__(
        self, parent, title: str, gef_type: str, types: List[str], required: str
    ):
        super().__init__()
        self.parent = parent
        self.gef_type: str = gef_type
        self.title: str = title
        self.types: List[str] = types
        self.required: bool = required == "True"

    def __str__(self):
        return (
            "GrammarElementFieldTypeValue("
            f"parent: {self.parent}, "
            f"title: {self.title}, "
            f"gef_type: {self.gef_type}({', '.join(self.types)}), "
            f"required: {self.required}"
            ")"
        )

    def _print_grammar_field_type(self):
        return (
            f"  - TITLE: {self.title}\n"
            f"    TYPE: {self.gef_type}({', '.join(self.types)})\n"
            f"    REQUIRED: {self.required!s}\n"
        )
