from typing import Optional

from strictdoc.backend.dsl.models.document_config import DocumentConfig
from strictdoc.core.document_meta import DocumentMeta


class Document:
    def __init__(
        self, name, title, config: DocumentConfig, free_texts, section_contents
    ):
        assert isinstance(free_texts, list)
        self.name = name if name else title
        self.config = config if config else DocumentConfig.default_config(self)
        self.free_texts = free_texts
        self.section_contents = section_contents

        self.ng_sections = []
        self.ng_level = 0
        self.ng_needs_generation = False
        self.meta: Optional[DocumentMeta] = None
        self.legacy_title_is_used = name is not None and len(name) > 0

    def __str__(self):
        return (
            f"Document("
            f"id: {id(self)}, "
            f"name: {self.name}, "
            f"section_contents: {self.section_contents})"
        )

    def __repr__(self):
        return self.__str__()

    def assign_meta(self, meta):
        assert isinstance(meta, DocumentMeta)
        self.meta = meta
