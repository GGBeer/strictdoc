from typing import Optional, List

from pybtex.database import BibliographyData, parse_file

from strictdoc.backend.sdoc.models.type_system import (
    BibEntry,
    BibFileEntry,
    FileEntryFormat,
    BibEntryFormat,
)
from strictdoc.helpers.auto_described import auto_described


@auto_described
class DocumentBibliography:
    def __init__(
        self,
        parent,
        bib_files: Optional[List[BibFileEntry]],
        bib_entries: Optional[List[BibEntry]],
    ):
        self.parent = parent
        self.bib_db = BibliographyData()
        self.bib_citations = set()

        self.bib_files = bib_files
        self.parsed_bib_files = 0
        self.bib_entries = bib_entries
        self.parsed_bib_entries = 0



    def parse_bib_entries(self ):
        if self.bib_entries and len(self.bib_entries) > 0 and\
                self.parsed_bib_entries == 0:
            for entry in self.bib_entries:
                entry.parse_bib_entry()
                if entry.bibtex_entry:
                    self.bib_db.add_entry(entry.ref_cite, entry.bibtex_entry)
                # BibTex Entries in the Bibliography are not included as citation
                if entry.bib_format != BibEntryFormat.BIBTEX:
                    self.bib_citations.add(entry.ref_cite)
                self.parsed_bib_entries += 1

    def parse_bib_files(self):
        if self.bib_files and len(self.bib_files) > 0 and self.parsed_bib_files == 0:
            for bib_file in self.bib_files:
                assert bib_file.g_file_format == FileEntryFormat.BIBTEX
                # Only Bibtex files are suppported!
                bibtex_db = parse_file(
                    bib_file.g_file_path, bib_format="bibtex"
                )
                for bib_entry in bibtex_db.entries:
                    self.bib_db.add_entry(
                        bib_entry, bibtex_db.entries[bib_entry]
                    )
                self.parsed_bib_files += 1
