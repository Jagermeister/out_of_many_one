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
STORAGE.database_tables_create_and_populate()

for report in reports:
    report.insert(0, hash_from_strings(report))
    STORAGE.report_add(tuple(report))

filers = STORAGE.filers_get()
filer_by_name = {}
for filer in filers:
    key = filer[1] + '+|+' + filer[2]
    filer_by_name[key] = filer[0]

filer_types = STORAGE.filer_types_get()
filer_type_by_name = {}
for filer_type in filer_types:
    filer_type_by_name[filer_type[1].lower()] = filer_type[0]

document_types = STORAGE.document_types_get()
document_type_by_name = {}
for document_type in document_types:
    document_type_by_name[document_type[1].lower()] = document_type[0]

PARSE = Parse()
reports_from_storage = STORAGE.reports_get()
for report in reports_from_storage:
    (key, hashcode, name_first, name_last, filer_type, document_link, filed_date) = report
    (document_type, document_id, document_name) = PARSE.document_link_parse(document_link)
    try:
        filer_type_key = filer_type_by_name[filer_type.lower()]
        document_type = PARSE.document_type_standardize(document_type.lower())
        document_type_key = document_type_by_name[document_type.lower()]
    except ValueError as value_exception:
        print(f'Skipping report - unable to parse document type. "{report}". "{value_exception}"')
        continue
    except KeyError as key_exception:
        print(f'Skipping report - unable to lookup type. "{report}". "{key_exception}"')
        continue

    name_first = name_first.lower()
    name_last = name_last.lower()
    filer_name_key = name_first + '+|+' + name_last
    if not (filer_name_key in filer_by_name):
        filer_key = STORAGE.filer_add((name_first, name_last))
        filer_by_name[filer_name_key] = filer_key
    
    filer_key = filer_by_name[filer_name_key]
    STORAGE.document_add((key, filer_key, filer_type_key, document_type_key, 
                         document_id, document_name, filed_date))
