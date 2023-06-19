from __future__ import annotations

from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from strictdoc.backend.sdoc.models.document import Document


class DocumentReference:
    _document: Document | None

    def __init__(self):
        self._document: Optional[Document] = None

    def get_document(self) -> Optional[Document]:
        return self._document

    def set_document(self, document):
        self._document = document
