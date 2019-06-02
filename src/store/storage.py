""" Interface for storing data """

import sqlite3

from src.store.sql import (
    DOCUMENT_LINK_CREATE,
    DOCUMENT_LINKS_ANNUAL_REPORT_GET,
    DOCUMENT_TYPES_READ,
    DOCUMENT_TYPE_DEFAULTS,
    DOCUMENT_TYPE_POPULATE,
    FILER_CREATE,
    FILERS_READ,
    FILER_TYPE_DEFAULTS,
    FILER_TYPE_POPULATE,
    FILER_TYPES_READ,
    TABLES_CREATION,
    TABLE_INDEXES_CREATION,
    TABLES_POPULATE_DATA,
    REPORT_ANNUAL_RAW_CREATE,
    REPORT_ANNUALS_READ,
    REPORT_ANNUAL_CHARITY_CREATE,
    REPORT_ANNUAL_EARNED_INCOME_CREATE,
    REPORT_ANNUAL_ASSET_CREATE,
    REPORT_ANNUAL_PTR_CREATE,
    REPORT_ANNUAL_TRANSACTION_CREATE,
    REPORT_ANNUAL_GIFT_CREATE,
    REPORT_ANNUAL_TRAVEL_CREATE,
    REPORT_ANNUAL_LIABILITY_CREATE,
    REPORT_ANNUAL_POSITION_CREATE,
    REPORT_ANNUAL_AGREEMENT_CREATE,
    DOCUMENT_LINK_RAW_CREATE,
    DOCUMENT_LINK_RAWS_READ,
    DOCUMENT_LINK_RAWS_NOT_PARSED
)

DATABASE_NAME = './data/efd.db'

class Storage():
    """ Data storage implementation """

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()
        self.is_ready = False
        self._filers_by_name = {}

    def save(self):
        """ Save all current transactions """
        self.connection.commit()

    def close(self):
        """ Close all open connections """
        self.connection.close()

    def database_tables_create_and_populate(self):
        """ Create all tables not existing within the database """
        for table in TABLES_CREATION:
            self.cursor.execute(table)

        self.cursor.executescript(TABLE_INDEXES_CREATION)
        for filer_type_default in FILER_TYPE_DEFAULTS:
            self.cursor.execute(FILER_TYPE_POPULATE, filer_type_default)

        for document_type_default in DOCUMENT_TYPE_DEFAULTS:
            self.cursor.execute(DOCUMENT_TYPE_POPULATE, document_type_default)

        self.save()
        self.is_ready = True

    def annual_report_raw_add(self, annual_report):
        """ Annual Report to storage """
        self.cursor.execute(REPORT_ANNUAL_RAW_CREATE, annual_report)
        self.save()
        return self.cursor.lastrowid

    def annual_reports_get(self):
        """ Select all Annual Reports """
        self.cursor.execute(REPORT_ANNUALS_READ)
        return self.cursor.fetchall()

    def annual_report_charity_add(self, charity):
        self.cursor.executemany(REPORT_ANNUAL_CHARITY_CREATE, charity)
        self.save()

    def annual_report_earned_income_add(self, earned_income):
        self.cursor.executemany(REPORT_ANNUAL_EARNED_INCOME_CREATE, earned_income)
        self.save()

    def annual_report_asset_add(self, asset):
        self.cursor.executemany(REPORT_ANNUAL_ASSET_CREATE, asset)
        self.save()

    def annual_report_ptr_add(self, ptr):
        self.cursor.executemany(REPORT_ANNUAL_PTR_CREATE, ptr)
        self.save()

    def annual_report_transaction_add(self, transaction):
        self.cursor.executemany(REPORT_ANNUAL_TRANSACTION_CREATE, transaction)
        self.save()

    def annual_report_gift_add(self, gift):
        self.cursor.executemany(REPORT_ANNUAL_GIFT_CREATE, gift)
        self.save()

    def annual_report_travel_add(self, travel):
        self.cursor.executemany(REPORT_ANNUAL_TRAVEL_CREATE, travel)
        self.save()

    def annual_report_liability_add(self, liability):
        self.cursor.executemany(REPORT_ANNUAL_LIABILITY_CREATE, liability)
        self.save()

    def annual_report_position_add(self, position):
        self.cursor.executemany(REPORT_ANNUAL_POSITION_CREATE, position)
        self.save()

    def annual_report_agreement_add(self, agreement):
        self.cursor.executemany(REPORT_ANNUAL_AGREEMENT_CREATE, agreement)
        self.save()

    def document_types_get(self):
        """ Select all document_types """
        self.cursor.execute(DOCUMENT_TYPES_READ)
        return self.cursor.fetchall()

    def document_link_add(self, document):
        """ Add document to storage
        Args:
            document: tuple or list(tuple) - report_key, filer_key,
                filer_type_key, document_type_key, unique_id,
                document_name, document_date
        """
        command = self.cursor.executemany if isinstance(document, list) else self.cursor.execute
        command(DOCUMENT_LINK_CREATE, document)
        self.save()

    def document_links_annual_report(self):
        """ Annual Report document links """
        self.cursor.execute(DOCUMENT_LINKS_ANNUAL_REPORT_GET)
        return self.cursor.fetchall()

    def document_links_unparsed_get(self):
        """ Find all unparsed document links """
        self.cursor.execute(DOCUMENT_LINK_RAWS_NOT_PARSED)
        return self.cursor.fetchall()

    def filer_add(self, filer):
        """ Add filer to storage
        Args:
            filer: tuple - name_first, name_last
        """
        self.cursor.execute(FILER_CREATE, filer)
        self.save()
        return self.cursor.lastrowid

    def filers_get(self):
        """ Select all filers """
        self.cursor.execute(FILERS_READ)
        return self.cursor.fetchall()

    def filers_set_cache(self):
        """ Fill filer cache """
        filers = self.filers_get()
        self._filers_by_name = {}
        for filer in filers:
            filer_name_key = f'{filer[1]}+|+{filer[2]}'
            self._filers_by_name[filer_name_key] = filer[0]

    def filer_get_key(self, name_first, name_last):
        """ Find or add filer """
        if not self._filers_by_name:
            self.filers_set_cache()

        first = name_first.lower()
        last = name_last.lower()
        filer_name_key = f'{first}+|+{last}'
        if filer_name_key not in self._filers_by_name:
            filer_key = self.filer_add((first, last))
            self._filers_by_name[filer_name_key] = filer_key

        return self._filers_by_name[filer_name_key]

    def filer_types_get(self):
        """ Select all filer_types """
        self.cursor.execute(FILER_TYPES_READ)
        return self.cursor.fetchall()

    def document_link_raw_add(self, report):
        """ Add raw document links
        Args:
            report: tuple or list(tuple) - report_hash, name_first,
                name_last, filer_type, report_type, filed_date
        """
        command = self.cursor.executemany if isinstance(report, list) else self.cursor.execute
        command(DOCUMENT_LINK_RAW_CREATE, report)
        self.save()

    def document_link_raws_get(self):
        """ Select all document_link_raws """
        self.cursor.execute(DOCUMENT_LINK_RAWS_READ)
        return self.cursor.fetchall()
