STRICTDOC_BASIC_TYPE_SYSTEM = r"""
FieldName[noskipws]:
  /[A-Z]+[A-Z_]*/
;

SingleLineString:
  (!MultiLineStringStart /./)*
;

MultiLineStringStart[noskipws]:
  '>>>' '\n'
;

MultiLineStringEnd[noskipws]:
  '<<<'
;

MultiLineString[noskipws]:
  MultiLineStringStart-
  ((!MultiLineStringEnd /(?ms)./)+ | '')
  MultiLineStringEnd-
;

Reference[noskipws]:
  // FileReference is an early, experimental feature. Do not use yet.
  ParentReqReference | FileReference | BibReference
;

ParentReqReference[noskipws]:
  '- TYPE: Parent' '\n'
  '  VALUE: ' ref_uid = /.*$/ '\n'
;

FileReference[noskipws]:
  // FileReference is an early, experimental feature. Do not use yet.
  '- TYPE: File' '\n'
  file_entry = FileEntry
;

BibFileEntry[noskipws]:
  '- FORMAT: BibTex\n'
  '  VALUE: ' file_path = /.*$/ '\n'
;

FileEntry[noskipws]:
 ('  FORMAT: ' file_format = FileEntryFormat '\n')?
  '  VALUE: ' file_path = /.*$/ '\n'
;

FileEntryFormat[noskipws]:
  'BibTex' | 'Sourcecode' | 'Python' | /[A-Z]+[A-Z_]*/
;

BibReference[noskipws]:
  '- TYPE: BibRef' '\n'
 ('  FORMAT: ' bib_format = BibEntryFormat '\n')?
  '  VALUE: ' bib_value = /.*$/ '\n'
;

BibEntry[noskipws]:
  ('- FORMAT: ' bib_format = BibEntryFormat '\n'
   '  VALUE: ' bib_value = /.*$/ '\n'
  ) |
  (
   '- VALUE: ' bib_value = /.*$/ '\n'
  )
;

BibEntryFormat[noskipws]:
  'String' | 'BibTex' | 'Citation'
;

"""
