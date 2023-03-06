from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

from tests.end2end.helpers.screens.document.form_edit_config import (
    Form_EditConfig,
)
from tests.end2end.helpers.screens.document.form_edit_grammar import (
    Form_EditGrammar,
)
from tests.end2end.helpers.screens.document.form_edit_requirement import (
    Form_EditRequirement,
)
from tests.end2end.helpers.screens.document.form_edit_section import (
    Form_EditSection,
)


class Screen_Document:  # pylint: disable=invalid-name
    def __init__(self, test_case: BaseCase) -> None:
        assert isinstance(test_case, BaseCase)
        self.test_case: BaseCase = test_case

    def assert_on_screen(self):
        self.test_case.assert_element(
            '//body[@data-viewtype="document"]',
            by=By.XPATH,
        )

    def assert_empty_document(self) -> None:
        self.test_case.assert_element(
            '//*[@data-testid="document-placeholder"]'
        )

    def assert_not_empty_document(self) -> None:
        self.test_case.assert_element_not_visible(
            '//*[@data-testid="document-placeholder"]'
        )

    def assert_is_document_title(self, document_title: str) -> None:
        self.test_case.assert_text(document_title)

    def assert_text(self, text: str) -> None:
        self.test_case.assert_text(text)

    def assert_no_text(self, text: str) -> None:
        self.test_case.assert_element_not_present(
            f"//*[contains(., '{text}')]", by=By.XPATH
        )

    def assert_requirement_style_simple(self) -> None:
        # Make sure that the normal (not table-based) requirement is rendered.
        self.test_case.assert_element(
            '//sdoc-node[@data-testid="node-requirement-simple"]',
            by=By.XPATH,
        )

    def assert_requirement_style_table(self) -> None:
        # Make sure that the table-based requirement is rendered.
        self.test_case.assert_element(
            '//sdoc-node[@data-testid="node-requirement-table"]',
            by=By.XPATH,
        )

    def assert_toc_contains_string(self, string: str) -> None:
        self.test_case.assert_element(
            f"//turbo-frame[@id='frame-toc']//*[contains(., '{string}')]"
        )

    def do_open_edit_form(self) -> Form_EditRequirement:
        self.test_case.hover_and_click(
            hover_selector="(//sdoc-node)[2]",
            click_selector=(
                '(//sdoc-node)[2]//*[@data-testid="node-edit-action"]'
            ),
            hover_by=By.XPATH,
            click_by=By.XPATH,
        )
        return Form_EditRequirement(self.test_case)

    def do_open_config_form(self) -> Form_EditConfig:
        self.test_case.hover_and_click(
            hover_selector="(//sdoc-node)[1]",
            click_selector=(
                '(//sdoc-node)[1]//*[@data-testid="document-edit-config-action"]'  # noqa: E501
            ),
            hover_by=By.XPATH,
            click_by=By.XPATH,
        )
        return Form_EditConfig(self.test_case)

    def do_open_edit_grammar_modal(self) -> Form_EditGrammar:
        self.test_case.assert_element_not_present("//sdoc-modal", by=By.XPATH)
        self.test_case.click_xpath(
            '(//*[@data-testid="document-edit-grammar-action"])'
        )
        self.test_case.assert_element(
            "//sdoc-modal",
            by=By.XPATH,
        )
        return Form_EditGrammar(self.test_case)

    def do_export_reqif(self) -> None:
        self.test_case.click_xpath(
            '(//*[@data-testid="document-export-reqif-action"])'
        )

    def do_open_node_menu(self, field_order: int = 1) -> None:
        self.test_case.hover_and_click(
            hover_selector=f"(//sdoc-node)[{field_order}]",
            click_selector=(
                f"(//sdoc-node)[{field_order}]"
                "//*[@data-testid='node-menu-handler']"
            ),
            hover_by=By.XPATH,
            click_by=By.XPATH,
        )

    def assert_field_contains(self, field_tag: str, text: str) -> None:
        self.test_case.assert_element(
            f"//{field_tag}"
            f"[contains(., '{text}')]",
            by=By.XPATH
        )

    # Add section

    def do_node_add_section_first(self, field_order: int = 1) -> Form_EditSection:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-section-first-action"]'
            ),
            by=By.XPATH,
        )
        return Form_EditSection(self.test_case)

    def do_node_add_section_above(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-section-above-action"]'
            ),
            by=By.XPATH,
        )

    def do_node_add_section_below(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-section-below-action"]'
            ),
            by=By.XPATH,
        )

    def do_node_add_section_child(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-section-child-action"]'
            ),
            by=By.XPATH,
        )

    # Add requirement

    def do_node_add_requirement_first(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-requirement-first-action"]'
            ),
            by=By.XPATH,
        )

    def do_node_add_requirement_above(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-requirement-above-action"]'
            ),
            by=By.XPATH,
        )

    def do_node_add_requirement_below(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-requirement-below-action"]'
            ),
            by=By.XPATH,
        )

    def do_node_add_requirement_child(self, field_order: int = 1) -> None:
        self.test_case.click(
            selector=(
                f"(//sdoc-node)[{field_order}]"
                '//*[@data-testid="node-add-requirement-child-action"]'
            ),
            by=By.XPATH,
        )
