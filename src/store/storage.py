""" Interface for storing data """

import sqlite3

from src.store.sql import (
    DOCUMENT_LINK_CREATE,
    DOCUMENT_LINKS_ANNUAL_REPORT_GET,
    DOCUMENT_TYPES_READ,
    FILER_CREATE,
    FILERS_READ,
    FILER_TYPES_READ,
    TABLES_CREATION,
    TABLES_POPULATE_DATA,
    REPORT_ANNUAL_RAW_CREATE,
    REPORT_ANNUALS_READ,
    REPORT_ANNUAL_CHARITY_CREATE,
    REPORT_ANNUAL_EARNED_INCOME_CREATE,
    REPORT_ANNUAL_ASSET_CREATE,
    REPORT_ANNUAL_PTR_CREATE,
    REPORT_ANNUAL_TRANSACTION_CREATE,
    REPORT_CREATE,
    REPORTS_READ
)

DATABASE_NAME = './data/efd.db'

class Storage():
    """ Data storage implementation """

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()

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
            self.save()

        #for table in TABLES_POPULATE_DATA:
        #    self.cursor.execute(table)
        #    self.save()

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

    def filer_types_get(self):
        """ Select all filer_types """
        self.cursor.execute(FILER_TYPES_READ)
        return self.cursor.fetchall()

    def report_add(self, report):
        """ Add raw report details
        Args:
            report: tuple or list(tuple) - report_hash, name_first,
                name_last, filer_type, report_type, filed_date
        """
        command = self.cursor.executemany if isinstance(report, list) else self.cursor.execute
        command(REPORT_CREATE, report)
        self.save()

    def reports_get(self):
        """ Select all reports """
        self.cursor.execute(REPORTS_READ)
        return self.cursor.fetchall()
