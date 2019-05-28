""" Entry point for _Out of many, one_ attempt to capture, transform,
    and report on United States Senators' Financial Disclosures.  """

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

reports_from_storage = STORAGE.reports_get()
print(reports_from_storage)
