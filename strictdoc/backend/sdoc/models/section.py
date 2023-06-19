import uuid
from typing import List, Optional

from strictdoc.backend.sdoc.document_reference import DocumentReference
from strictdoc.backend.sdoc.models.free_text import FreeText
from strictdoc.backend.sdoc.models.node import Node
from strictdoc.helpers.auto_described import auto_described


@auto_described
class SectionContext:
    def __init__(self):
        self.title_number_string = None


@auto_described
class Section(Node):  # pylint: disable=too-many-instance-attributes
    def __init__(  # pylint: disable=too-many-arguments
        self,
        parent,
        uid,
        custom_level: Optional[str],
        title,
        requirement_prefix: Optional[str],
        section_contents: List[Node],
    ):
        self.parent = parent

        # TODO: Remove .uid, keep reserved_uid only.
        meaningful_uid: Optional[str] = None
        if uid is not None and len(uid) > 0:
            meaningful_uid = uid
        self.uid: Optional[str] = meaningful_uid
        self.reserved_uid: Optional[str] = meaningful_uid

        self.title = title
        self.requirement_prefix: Optional[str] = requirement_prefix
        self.section_contents = section_contents

        # HEF4
        self.custom_level: Optional[str] = custom_level
        self.ng_resolved_custom_level: Optional[str] = custom_level

        self.ng_level: Optional[int] = None
        self.ng_has_requirements = False
        self.ng_document_reference: Optional[DocumentReference] = None
        self.context = SectionContext()
        self.node_id = uuid.uuid4().hex

    @staticmethod
    def get_type_string() -> str:
        return "section"

    @property
    def document(self):
        return self.ng_document_reference.get_document()

    @property
    def is_requirement(self):
        return False

    @property
    def is_composite_requirement(self):
        return False

    @property
    def is_section(self):
        return True

    @property
    def is_freetext(self):
        return False

    @property
    def has_freetext(self) -> bool:
        for item in self.section_contents:
            if isinstance(item, FreeText):
                return True
        return False

    def get_freetext(self) -> List[FreeText]:
        freetext: List[FreeText] = []
        for item in self.section_contents:
            if isinstance(item, FreeText):
                freetext.append(item)
        return freetext

    def add_freetext(self, freetext: Optional[FreeText]):
        if freetext is None:
            return
        self.section_contents.append(freetext)
