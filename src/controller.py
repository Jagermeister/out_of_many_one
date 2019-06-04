""" Managers interactions between Fetching, Parsing, and Storing """

import logging

from src.parse.parse import Parse
from src.scrape.efd import EFD
from src.store.storage import Storage
from src.utility import hash_from_strings

class Controller:
    """ Control interaction between Fetching, Parsing, and Storage """

    def __init__(self):
        """ Create concrete implementations """
        self.fetcher = EFD()
        self.parser = Parse()
        self.storer = Storage()

    def _fetcher_make_ready(self):
        """ Ensure fetching is setup """
        if not self.fetcher.is_ready:
            self.fetcher.login()

    def _storer_make_ready(self):
        """ Ensure storage is setup """
        if not self.storer.is_ready:
            self.storer.database_tables_create_and_populate()

    def fetch_new_document_links(self):
        logging.info("Fetching document links...")
        self._fetcher_make_ready()
        fetched = self.fetcher.annual_reports_search()
        logging.info(f"Found '{len(fetched)}' document links!")

        self._storer_make_ready()
        stored = self.storer.document_link_raws_get()
        logging.info(f"Retrieved '{len(stored)}' document links from storage.")

        reports_added = 0
        reports_seen = frozenset([seen[1] for seen in stored])
        for report in fetched:
            hash_key = hash_from_strings(report)
            if hash_key not in reports_seen:
                report.insert(0, hash_key)
                self.storer.document_link_raw_add(tuple(report))
                reports_added += 1

        logging.info(f"Added '{reports_added}' raw document links.")

    def parse_document_links(self):
        self._storer_make_ready()
        document_links = self.storer.document_links_unparsed_get()
        logging.info(f"Parsing '{len(document_links)}' raw document links.'")
        document_link_processed = 0
        for document_link in document_links:
            (key, name_first, name_last, filer_type, document_href, filed_date) = document_link
            (document_type, document_id, document_name) = self.parser.document_link_parse(document_href)

            filer_key = self.storer.filer_get_key(name_first, name_last)
            filer_type_key = self.storer.filer_type_by_name(filer_type.lower())
            document_type_key = self.storer.document_type_by_name(document_type.lower())
            is_paper = int(document_type.lower() == "unknown")
            self.storer.document_link_add(
                (key, filer_key, filer_type_key, document_type_key, 
                is_paper, document_id, document_name, filed_date))
            document_link_processed += 1
        
        logging.info(f"Parsed '{document_link_processed}' raw document links.")

    def fetch_new_annual_reports(self):
        self._storer_make_ready()
        document_links = self.storer.document_links_annual_report()
        logging.info(f"Retrieved '{len(document_links)}' document links from storage.")

        reports_added = 0
        self._fetcher_make_ready()
        for document_link in document_links:
            link_key, document_id = document_link
            header, sections = self.fetcher.annual_report_view(document_id)

            annual_report = [link_key, str(header)]
            annual_report.extend([str(s) for s in sections])
            self.storer.annual_report_raw_add(annual_report)
            reports_added += 1
            if reports_added % 10 == 0:
                logging.info(f".. '{reports_added}' raw annual reports added ..")

        logging.info(f"Added '{reports_added}' raw annual reports.")

    def parse_annual_reports(self):
        self._storer_make_ready()
        annual_reports = self.storer.annual_reports_get()
        print(len(annual_reports))
        #for report in annual_reports:
        #    print(report)
