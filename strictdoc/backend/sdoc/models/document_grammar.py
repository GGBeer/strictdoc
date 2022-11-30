from collections import defaultdict, OrderedDict
from typing import List, Set, Dict
from strictdoc.backend.sdoc.models.type_system import (
    GrammarElementField,
    GrammarElementFieldString,
    GrammarElementFieldTypeValue,
    GrammarReferenceType,
    RequirementFieldName,
    RESERVED_NON_META_FIELDS,
    RequirementFieldType,
)


class GrammarElement:
    def __init__(self, parent, tag: str, fields: List[GrammarElementField]):
        self.parent = parent
        self.tag: str = tag
        self.fields: List[GrammarElementField] = fields
        fields_map: OrderedDict = OrderedDict()
        for field in fields:
            fields_map[field.title] = field
        self.fields_map = fields_map

    def enumerate_meta_field_titles(self):
        for field in self.fields:
            if field.title in (
                RequirementFieldName.TITLE,
                RequirementFieldName.STATEMENT,
            ):
                break
            if field.title in RESERVED_NON_META_FIELDS:
                continue
            yield field.title

    def enumerate_custom_content_field_titles(self):
        after_title_or_statement = False
        for field in self.fields:
            if field.title in (
                RequirementFieldName.TITLE,
                RequirementFieldName.STATEMENT,
            ):
                after_title_or_statement = True
            if field.title in RESERVED_NON_META_FIELDS:
                continue
            if not after_title_or_statement:
                continue
            yield field.title


class DocumentGrammar:
    def __init__(self, parent, elements: List[GrammarElement]):
        self.parent = parent
        self.elements: List[GrammarElement] = elements

        registered_elements: Set[str] = set()
        elements_by_type: Dict[str, GrammarElement] = {}
        fields_by_type: Dict[str, Set[str]] = defaultdict(set)

        for element in elements:
            registered_elements.add(element.tag)
            elements_by_type[element.tag] = element
            for element_field in element.fields:
                fields_by_type[element.tag].add(element_field.title)

        self.registered_elements: Set[str] = registered_elements
        self.elements_by_type: Dict[str, GrammarElement] = elements_by_type
        self.fields_order_by_type: Dict[str, Set[str]] = fields_by_type

        self.is_default = False

    @staticmethod
    def create_default(parent):
        fields = [
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.UID,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.LEVEL,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.STATUS,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
            GrammarElementFieldString(
                # TODO GrammarElementFieldString => GrammarElementFieldTag
                parent=None,
                title=RequirementFieldName.TAGS,
                gef_type=RequirementFieldType.TAG,
                required="False",
            ),
            GrammarElementFieldTypeValue(
                parent=None,
                title=RequirementFieldName.REFS,
                gef_type=RequirementFieldType.TYPE_VALUE,
                types=[
                    GrammarReferenceType.PARENT_REQ_REFERENCE,
                    GrammarReferenceType.FILE_REFERENCE,
                    GrammarReferenceType.EXTERNAL_REFERENCE,
                ],
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.TITLE,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.STATEMENT,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.RATIONALE,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.COMMENT,
                gef_type=RequirementFieldType.STRING,
                required="False",
            ),
        ]
        requirement_element = GrammarElement(
            parent=None, tag="REQUIREMENT", fields=fields
        )
        elements: List[GrammarElement] = [requirement_element]
        grammar = DocumentGrammar(parent=parent, elements=elements)
        grammar.is_default = True

        return grammar

    def dump_fields(self, requirement_type) -> str:
        return ", ".join(
            list(
                map(
                    lambda g: g.title,
                    self.elements_by_type[requirement_type].fields,
                )
            )
        )
