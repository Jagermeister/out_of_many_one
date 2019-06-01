""" Entry point for _Out of many, one_ attempt to capture, transform,
    and report on United States Senators' Financial Disclosures.  """

from src.parse.parse import Parse
from src.scrape.efd import EFD
from src.store.storage import Storage
from src.utility import hash_from_strings

def document_links_search_and_store(efd_app, efd_storage):
    reports = efd_app.search('booker')['data']
    for report in reports:
        report.insert(0, hash_from_strings(report))
        efd_storage.report_add(tuple(report))

def document_link_parse_and_store(efd_storage, efd_parse):
    # Setup lookup mappings
    # Candidate to be moved to store.Storage
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
   
    reports_from_storage = efd_storage.reports_get()
    for report in reports_from_storage:
        (key, _, name_first, name_last, filer_type, document_link, filed_date) = report
        (document_type, _, document_id, document_name) = efd_parse.document_link_parse(document_link)
        try:
            filer_type_key = filer_type_by_name[filer_type.lower()]
            document_type = efd_parse.document_type_standardize(document_type.lower())
            document_type_key = document_type_by_name[document_type.lower()]
        except ValueError as value_exception:
            print(f'Skipping report - unable to parse document type. "{report}". "{value_exception}"')
            continue
        except KeyError as key_exception:
            print(f'Skipping report - unable to lookup type. "{report}". "{key_exception}"')
            continue

        name_first = name_first.lower()
        name_last = name_last.lower()
        is_paper = int(document_type.lower() == "unknown")
        filer_name_key = name_first + '+|+' + name_last
        if not (filer_name_key in filer_by_name):
            filer_key = efd_storage.filer_add((name_first, name_last))
            filer_by_name[filer_name_key] = filer_key
        
        filer_key = filer_by_name[filer_name_key]
        efd_storage.document_link_add(
            (key, filer_key, filer_type_key, document_type_key, 
            is_paper, document_id, document_name, filed_date))

import time
def annual_report_fetch_and_store(efd_app, efd_storage):
    document_links = efd_storage.document_links_annual_report()
    for link in document_links:
        link_key, _, _, document_id = link
        time.sleep(2)
        print(link, flush=True)
        sections = efd_app.annual_report_view(document_id)
        sections = [str(s) for s in sections]
        sections.insert(0, link_key)
        efd_storage.annual_report_raw_add(sections)

def annual_reports_parse_and_store(efd_storage, efd_parse):
    annual_reports = efd_storage.annual_reports_get()
    #annual_reports = [efd_storage.annual_reports_get()[8]]
    for report in annual_reports:
        (report_key, link_key,
        one, two, three, four_a, four_b, five,
        six, seven, eight, nine, ten, comment) = report

        #print(report_key, four_a)
        #parse_testing(four_a)

        charity = efd_parse.annual_report_charity_parse(report_key, one)
        ##efd_storage.annual_report_charity_add(charity)

        earned_income = efd_parse.annual_report_earned_income_parse(report_key, two)
        ##efd_storage.annual_report_earned_income_add(earned_income)

        asset = efd_parse.annual_report_asset_parse(report_key, three)
        ##efd_storage.annual_report_asset_add(asset)

        ptr = efd_parse.annual_report_ptr_parse(report_key, four_a)
        ##efd_storage.annual_report_ptr_add(ptr)




#APP = EFD()
#APP.login()

STORAGE = Storage()
#STORAGE.database_tables_create_and_populate()

PARSE = Parse()

#document_links_search_and_store(APP, STORAGE)
#document_link_parse_and_store(STORAGE, PARSE)
#annual_report_fetch_and_store(APP, STORAGE)
annual_reports_parse_and_store(STORAGE, PARSE)
