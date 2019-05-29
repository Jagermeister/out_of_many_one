""" Entry point for _Out of many, one_ attempt to capture, transform,
    and report on United States Senators' Financial Disclosures.  """

from src.parse.parse import Parse
from src.scrape.efd import EFD
from src.store.storage import Storage
from src.utility import hash_from_strings


APP = EFD()
APP.login()
reports = APP.search('booker')['data']

STORAGE = Storage()
STORAGE.database_tables_create()

for report in reports:
    report.insert(0, hash_from_strings(report))
    STORAGE.report_add(tuple(report))

PARSE = Parse()
reports_from_storage = STORAGE.reports_get()
for report in reports_from_storage:
    (key, hashcode, name_first, name_last, filter_type, document_link, filed_date) = report
    (document_type, document_id, document_name) = PARSE.document_link_parse(document_link)
    print(key, document_type, document_id, document_name)
