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
        if not self.fetcher.is_logged_in:
            self.fetcher.login()

    def fetch_new_document_links(self):
        logging.info("Fetching document links...")
        self._fetcher_make_ready()
        fetched = self.fetcher.annual_reports_search()
        logging.info(f"Found '{len(fetched)}' document links!")

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

        logging.info(f"Added '{reports_added}' new document links.")
