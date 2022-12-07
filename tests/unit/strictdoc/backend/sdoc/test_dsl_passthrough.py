from strictdoc.backend.sdoc.models.document import Document
from strictdoc.backend.sdoc.models.requirement import (
    Requirement,
    CompositeRequirement,
)
from strictdoc.backend.sdoc.models.type_system import ReferenceType
from strictdoc.backend.sdoc.models.section import Section
from strictdoc.backend.sdoc.reader import SDReader
from strictdoc.backend.sdoc.writer import SDWriter


def test_001_minimal_doc():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]

[REQUIREMENT]

[REQUIREMENT]
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_002_minimal_req():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
TITLE: Hello
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_003_comments_01_several_comments():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
TITLE: Hello
COMMENT: Comment #1
COMMENT: Comment #2
COMMENT: Comment #3
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_003_comments_02_single_line_empty():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
COMMENT:
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_003_comments_02_single_line_empty_and_space():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
COMMENT: 
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_003_comments_03_multiline_empty():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
COMMENT: >>>
<<<
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_004_several_tags():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
TAGS: A, B, C, D
TITLE: Hello
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_010_multiple_sections():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[REQUIREMENT]
STATEMENT: >>>
This is a statement 1
This is a statement 2
This is a statement 3
<<<

[/SECTION]

[SECTION]
TITLE: Test Section

[REQUIREMENT]
STATEMENT: >>>
This is a statement 1
This is a statement 2
This is a statement 3
<<<

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output


def test_020_free_text():
    input = """
[DOCUMENT]
TITLE: Test Doc

[FREETEXT]
Hello world
[/FREETEXT]
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_021_freetext_empty():
    input = """
[DOCUMENT]
TITLE: Test Doc

[FREETEXT]
[/FREETEXT]
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_022_free_text_inline_link():
    input = """
[DOCUMENT]
TITLE: Test Doc

[FREETEXT]
String 1
String 2 [LINK: REQ-001] String 3
String 4
[/FREETEXT]
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_023_free_text_():
    input = """
[DOCUMENT]
TITLE: Test Doc

[FREETEXT]
AAA  [/FREETEXT]
[/FREETEXT]
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_030_multiline_statement():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[REQUIREMENT]
STATEMENT: >>>
This is a statement 1
This is a statement 2
This is a statement 3
<<<

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    assert isinstance(
        document.section_contents[0].section_contents[0], Requirement
    )
    requirement_1 = document.section_contents[0].section_contents[0]
    assert (
        requirement_1.statement_multiline
        == "This is a statement 1\nThis is a statement 2\nThis is a statement 3"
    )

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output


def test_036_rationale_single_line():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[REQUIREMENT]
STATEMENT: Some statement
RATIONALE: This is a Rationale

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output

    assert isinstance(
        document.section_contents[0].section_contents[0], Requirement
    )
    requirement_1 = document.section_contents[0].section_contents[0]
    assert requirement_1.rationale == "This is a Rationale"


def test_037_rationale_multi_line():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[REQUIREMENT]
STATEMENT: Some statement
RATIONALE: >>>
This is a Rationale line 1
This is a Rationale line 2
This is a Rationale line 3
<<<

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output

    assert isinstance(
        document.section_contents[0].section_contents[0], Requirement
    )
    requirement_1 = document.section_contents[0].section_contents[0]
    assert (
        requirement_1.rationale_multiline
        == "This is a Rationale line 1\nThis is a Rationale line 2\nThis is a Rationale line 3"
    )


def test_040_composite_requirement_1_level():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[COMPOSITE_REQUIREMENT]
STATEMENT: Some parent requirement statement
COMMENT: >>>
This is a body part 1
This is a body part 2
This is a body part 3
<<<

[REQUIREMENT]
STATEMENT: Some child requirement statement
COMMENT: >>>
This is a child body part 1
This is a child body part 2
This is a child body part 3
<<<

[/COMPOSITE_REQUIREMENT]

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output

    assert isinstance(
        document.section_contents[0].section_contents[0], CompositeRequirement
    )
    requirement_1 = document.section_contents[0].section_contents[0]
    assert requirement_1.ng_level == 2
    assert (
        requirement_1.comments[0].comment_multiline
        == "This is a body part 1\nThis is a body part 2\nThis is a body part 3"
    )


def test_042_composite_requirement_2_level():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[COMPOSITE_REQUIREMENT]
STATEMENT: 1.1 composite req statement
COMMENT: >>>
body composite 1.1
<<<

[COMPOSITE_REQUIREMENT]
STATEMENT: 1.1.1 composite req statement
COMMENT: >>>
body composite 1.1.1
<<<

[REQUIREMENT]
STATEMENT: 1.1.1.1 composite req statement
COMMENT: >>>
body 1.1.1.1
<<<

[/COMPOSITE_REQUIREMENT]

[/COMPOSITE_REQUIREMENT]

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output

    assert isinstance(
        document.section_contents[0].section_contents[0], CompositeRequirement
    )
    requirement_1_1 = document.section_contents[0].section_contents[0]
    assert requirement_1_1.ng_level == 2
    assert requirement_1_1.comments[0].comment_multiline == "body composite 1.1"

    assert isinstance(
        document.section_contents[0].section_contents[0].requirements[0],
        CompositeRequirement,
    )
    requirement_1_1_1 = (
        document.section_contents[0].section_contents[0].requirements[0]
    )
    assert requirement_1_1_1.ng_level == 3
    assert (
        requirement_1_1_1.comments[0].comment_multiline
        == "body composite 1.1.1"
    )

    assert isinstance(
        document.section_contents[0]
        .section_contents[0]
        .requirements[0]
        .requirements[0],
        Requirement,
    )
    requirement_1_1_1 = (
        document.section_contents[0]
        .section_contents[0]
        .requirements[0]
        .requirements[0]
    )
    assert requirement_1_1_1.ng_level == 4
    assert requirement_1_1_1.comments[0].comment_multiline == "body 1.1.1.1"


# This test is needed to make sure that the grammar details related
# to the difference of parting single vs multiline strings are covered.
def test_050_requirement_single_line_statement_one_symbol():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
STATEMENT: 1
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    document: Document = reader.read(sdoc_input)
    requirement = document.section_contents[0]
    assert requirement.statement == "1"

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_060_file_ref():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[REQUIREMENT]
REFS:
- TYPE: File
  VALUE: /tmp/sample.cpp
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    document: Document = reader.read(input_sdoc)
    requirement = document.section_contents[0]
    assert len(requirement.references) == 1
    assert requirement.references[0].ref_type == ReferenceType.FILE
    assert requirement.references[0].path == "/tmp/sample.cpp"

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output


def test_070_document_config_version():
    input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1

[REQUIREMENT]
REFS:
- TYPE: File
  VALUE: /tmp/sample.cpp
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    document: Document = reader.read(input)
    assert document.config.version == "0.0.1"

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_071_document_config_number():
    input = """
[DOCUMENT]
TITLE: Test Doc
UID: SDOC-01

[REQUIREMENT]
REFS:
- TYPE: File
  VALUE: /tmp/sample.cpp
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    document: Document = reader.read(input)
    assert document.config.uid == "SDOC-01"

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_072_document_config_classification():
    input = """
[DOCUMENT]
TITLE: Test Doc
UID: SDOC-01
VERSION: 0.0.1
CLASSIFICATION: Restricted

[REQUIREMENT]
REFS:
- TYPE: File
  VALUE: /tmp/sample.cpp
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    document: Document = reader.read(input)
    assert document.config.classification == "Restricted"

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_090_document_config_all_fields():
    input = """
[DOCUMENT]
TITLE: Test Doc
UID: SDOC-01
VERSION: 0.0.1
CLASSIFICATION: Restricted
OPTIONS:
  MARKUP: Text
  AUTO_LEVELS: Off
  REQUIREMENT_STYLE: Table
  REQUIREMENT_IN_TOC: True

[SECTION]
LEVEL: 123
TITLE: "Section"

[REQUIREMENT]
LEVEL: 456
STATEMENT: ABC

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    document: Document = reader.read(input)
    assert document.title == "Test Doc"
    assert document.config.version == "0.0.1"
    assert document.config.uid == "SDOC-01"
    assert document.config.classification == "Restricted"
    assert document.config.markup == "Text"
    assert document.config.auto_levels == False
    assert document.config.requirement_style == "Table"
    assert document.config.requirement_in_toc == "True"

    section = document.section_contents[0]
    assert isinstance(section, Section)
    assert section.level == "123"

    requirement = section.section_contents[0]
    assert isinstance(requirement, Requirement)
    assert requirement.level == "456"

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_100_basic_test():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Doc

[SECTION]
TITLE: Test Section

[REQUIREMENT]
TAGS: Tag 1, Tag 2, Tag 3
REFS:
- TYPE: File
  VALUE: /usr/local/bin/hexe
- TYPE: File
  VALUE: /usr/local/bin/hexe
- TYPE: File
  VALUE: /usr/local/bin/hexe
STATEMENT: System shall do X
COMMENT: This requirement is very important

[REQUIREMENT]
UID: REQ-001
STATUS: Draft
TITLE: Optional title B
STATEMENT: System shall do Y
COMMENT: This requirement is very important

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)
    assert isinstance(document, Document)

    assert isinstance(
        document.section_contents[0].section_contents[0], Requirement
    )
    requirement_1 = document.section_contents[0].section_contents[0]
    assert requirement_1.tags[0] == "Tag 1"
    assert requirement_1.tags[1] == "Tag 2"
    assert requirement_1.tags[2] == "Tag 3"

    writer = SDWriter()
    output = writer.write(document)

    assert input_sdoc == output


def test_081_document_config_markup_not_specified():
    input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1

[REQUIREMENT]
REFS:
- TYPE: File
  VALUE: /tmp/sample.cpp
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    document: Document = reader.read(input)
    assert document.config.version == "0.0.1"
    assert document.config.markup is None

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_081_document_config_markup_specified():
    input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1
OPTIONS:
  MARKUP: Text

[REQUIREMENT]
REFS:
- TYPE: File
  VALUE: /tmp/sample.cpp
""".lstrip()

    reader = SDReader()

    document = reader.read(input)
    assert isinstance(document, Document)

    document: Document = reader.read(input)
    assert document.config.version == "0.0.1"

    writer = SDWriter()
    output = writer.write(document)

    assert input == output


def test_082_document_config_auto_levels_specified_to_false():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1
OPTIONS:
  AUTO_LEVELS: Off
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    document: Document = reader.read(sdoc_input)
    assert document.config.auto_levels is False

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_083_requirement_level():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1
OPTIONS:
  AUTO_LEVELS: Off

[SECTION]
LEVEL: 123
TITLE: "Section"

[REQUIREMENT]
LEVEL: 456
STATEMENT: ABC

[/SECTION]
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    document: Document = reader.read(sdoc_input)
    assert document.config.auto_levels is False
    section = document.section_contents[0]
    assert section.level == "123"

    requirement = section.section_contents[0]
    assert isinstance(requirement, Requirement)
    assert requirement.level == "456"

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_085_options_requirement_style():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1
OPTIONS:
  REQUIREMENT_STYLE: Table
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    document: Document = reader.read(sdoc_input)
    assert document.config.requirement_style == "Table"

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_087_options_requirement_in_toc():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc
VERSION: 0.0.1
OPTIONS:
  REQUIREMENT_IN_TOC: True
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    document: Document = reader.read(sdoc_input)
    assert document.config.requirement_in_toc == "True"

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_150_grammar_minimal_doc():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[GRAMMAR]
ELEMENTS:
- TAG: LOW_LEVEL_REQUIREMENT
  FIELDS:
  - TITLE: CUSTOM_FIELD
    TYPE: String
    REQUIRED: True
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_151_grammar_single_choice():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[GRAMMAR]
ELEMENTS:
- TAG: LOW_LEVEL_REQUIREMENT
  FIELDS:
  - TITLE: SINGLE_CHOICE_FIELD
    TYPE: SingleChoice(A, B, C)
    REQUIRED: True

[LOW_LEVEL_REQUIREMENT]
SINGLE_CHOICE_FIELD: A
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_152_grammar_multiple_choice():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[GRAMMAR]
ELEMENTS:
- TAG: LOW_LEVEL_REQUIREMENT
  FIELDS:
  - TITLE: MULTIPLE_CHOICE_FIELD
    TYPE: MultipleChoice(A, B, C)
    REQUIRED: True

[LOW_LEVEL_REQUIREMENT]
MULTIPLE_CHOICE_FIELD: A, C
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output


def test_153_grammar_tag():
    sdoc_input = """
[DOCUMENT]
TITLE: Test Doc

[GRAMMAR]
ELEMENTS:
- TAG: LOW_LEVEL_REQUIREMENT
  FIELDS:
  - TITLE: TAG_FIELD
    TYPE: Tag
    REQUIRED: True

[LOW_LEVEL_REQUIREMENT]
TAG_FIELD: A, C
""".lstrip()

    reader = SDReader()

    document = reader.read(sdoc_input)
    assert isinstance(document, Document)

    writer = SDWriter()
    output = writer.write(document)

    assert sdoc_input == output
