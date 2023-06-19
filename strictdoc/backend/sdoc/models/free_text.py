import uuid
from typing import List, Optional

from strictdoc.backend.sdoc.models.anchor import Anchor
from strictdoc.backend.sdoc.models.inline_link import InlineLink
from strictdoc.backend.sdoc.models.node import Node
from strictdoc.helpers.auto_described import auto_described


@auto_described
class FreeText(Node):
    def __init__(self, parent, uid: Optional[str], parts: List):
        assert isinstance(parts, list)
        self.parent = parent

        # TODO: Remove .uid, keep reserved_uid only.
        meaningful_uid: Optional[str] = None
        if uid is not None and len(uid) > 0:
            meaningful_uid = uid
        self.uid: Optional[str] = meaningful_uid
        self.reserved_uid: Optional[str] = meaningful_uid

        self.parts = parts
        self.ng_level: Optional[int] = None
        self.ng_resolved_custom_level: Optional[str] = None
        self.node_id = uuid.uuid4().hex

    @property
    def is_requirement(self):
        return False

    @property
    def is_composite_requirement(self):
        return False

    @property
    def is_section(self):
        return False

    @property
    def is_freetext(self):
        return True

    def get_parts_as_text(self) -> str:
        # [LINK: SECTION-CUSTOM-GRAMMARS]
        text = ""
        for part in self.parts:
            if isinstance(part, str):
                text += part
            elif isinstance(part, InlineLink):
                text += "[LINK: "
                text += part.link
                text += "]"
            elif isinstance(part, Anchor):
                text += "[ANCHOR: "
                text += part.value
                if part.has_title:
                    text += ", "
                    text += part.title
                text += "]"
            else:
                raise NotImplementedError(part)
        return text


class FreeTextContainer(FreeText):
    def __init__(self, parts: List):
        super().__init__(None, None, parts)
