""" Interface for storing data """

import sqlite3

from src.store.sql import (
    TABLE_CREATIONS,
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

    def database_tables_create(self):
        """ Create all tables not existing within the database """
        for table in TABLE_CREATIONS:
            self.cursor.execute(table)
            self.save()

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
