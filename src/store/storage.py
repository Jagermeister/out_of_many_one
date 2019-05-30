""" Interface for storing data """

import sqlite3

from src.store.sql import (
    DOCUMENT_LINK_CREATE,
    DOCUMENT_TYPES_READ,
    FILER_CREATE,
    FILERS_READ,
    FILER_TYPES_READ,
    TABLES_CREATION,
    TABLES_POPULATE_DATA,
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

        for table in TABLES_POPULATE_DATA:
            self.cursor.execute(table)
            self.save()

    def document_add(self, document):
        """ Add document to storage
        Args:
            document: tuple or list(tuple) - report_key, filer_key,
                filer_type_key, document_type_key, unique_id,
                document_name, document_year, document_date
        """
        command = self.cursor.executemany if isinstance(document, list) else self.cursor.execute
        command(DOCUMENT_LINK_CREATE, document)
        self.save()

    def document_types_get(self):
        """ Select all document_types """
        self.cursor.execute(DOCUMENT_TYPES_READ)
        return self.cursor.fetchall()

    def filer_add(self, filer):
        """ Add filer to storage
        Args:
            filer: tuple or list(tuple) - name_first, name_last
        """
        command = self.cursor.executemany if isinstance(filer, list) else self.cursor.execute
        command(FILER_CREATE, filer)
        self.save()

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
