""" Interface for storing data """

import sqlite3

from src.store.config import DATABASE_NAME
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
    REPORT_ANNUAL_CREATE,
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
    REPORT_ANNUAL_COMPENSATION_CREATE,
    REPORT_ANNUAL_ATTACHMENT_CREATE,
    DOCUMENT_LINK_RAW_CREATE,
    DOCUMENT_LINK_RAWS_READ,
    DOCUMENT_LINK_RAWS_NOT_PARSED
)
from typing import Any


class Storage():
    """ Data storage implementation """

    def __init__(self) -> None:
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()
        self.is_ready = False
        self._filers_by_name = {}
        self._filer_types_by_name = {}
        self._document_types_by_name = {}

    def save(self) -> None:
        """ Save all current transactions """
        self.connection.commit()

    def database_tables_create_and_populate(self) -> None:
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

    def annual_report_raw_add(self, annual_report) -> int:
        """ Annual Report to storage """
        self.cursor.execute(REPORT_ANNUAL_RAW_CREATE, annual_report)
        self.save()
        return self.cursor.lastrowid

    def annual_reports_get(self) -> list:
        """ Select all Annual Reports """
        self.cursor.execute(REPORT_ANNUALS_READ)
        return self.cursor.fetchall()

    def annual_report_add(self, report) -> None:
        self.cursor.execute(REPORT_ANNUAL_CREATE, report)
        self.save()

    def annual_report_charity_add(self, charity) -> None:
        self.cursor.executemany(REPORT_ANNUAL_CHARITY_CREATE, charity)
        self.save()

    def annual_report_earned_income_add(self, earned_income) -> None:
        self.cursor.executemany(REPORT_ANNUAL_EARNED_INCOME_CREATE, earned_income)
        self.save()

    def annual_report_asset_add(self, asset) -> None:
        self.cursor.executemany(REPORT_ANNUAL_ASSET_CREATE, asset)
        self.save()

    def annual_report_ptr_add(self, ptr) -> None:
        self.cursor.executemany(REPORT_ANNUAL_PTR_CREATE, ptr)
        self.save()

    def annual_report_transaction_add(self, transaction) -> None:
        self.cursor.executemany(REPORT_ANNUAL_TRANSACTION_CREATE, transaction)
        self.save()

    def annual_report_gift_add(self, gift) -> None:
        self.cursor.executemany(REPORT_ANNUAL_GIFT_CREATE, gift)
        self.save()

    def annual_report_travel_add(self, travel) -> None:
        self.cursor.executemany(REPORT_ANNUAL_TRAVEL_CREATE, travel)
        self.save()

    def annual_report_liability_add(self, liability) -> None:
        self.cursor.executemany(REPORT_ANNUAL_LIABILITY_CREATE, liability)
        self.save()

    def annual_report_position_add(self, position) -> None:
        self.cursor.executemany(REPORT_ANNUAL_POSITION_CREATE, position)
        self.save()

    def annual_report_agreement_add(self, agreement) -> None:
        self.cursor.executemany(REPORT_ANNUAL_AGREEMENT_CREATE, agreement)
        self.save()

    def annual_report_compensation_add(self, compensation) -> None:
        self.cursor.executemany(REPORT_ANNUAL_COMPENSATION_CREATE, compensation)
        self.save()

    def annual_report_attachment_add(self, attachment) -> None:
        self.cursor.executemany(REPORT_ANNUAL_ATTACHMENT_CREATE, attachment)
        self.save()

    def _document_types_get(self) -> list:
        """ Select all document_types """
        self.cursor.execute(DOCUMENT_TYPES_READ)
        return self.cursor.fetchall()

    def document_type_by_name(self, document_type_name: str) -> int:
        """ Fetch and cache by name """
        if not self._document_types_by_name:
            document_types = self._document_types_get()
            for document_type in document_types:
                key = document_type[0]
                name = document_type[1].lower()
                self._document_types_by_name[name] = key

        if document_type_name not in self._document_types_by_name:
            document_type_name = "unknown"

        return self._document_types_by_name[document_type_name]

    def document_link_add(self, document) -> None:
        """ Add document to storage
        Args:
            document: tuple or list(tuple) - report_key, filer_key,
                filer_type_key, document_type_key, unique_id,
                document_name, document_date
        """
        command = self.cursor.executemany if isinstance(document, list) else self.cursor.execute
        command(DOCUMENT_LINK_CREATE, document)
        self.save()

    def document_links_annual_report(self) -> list:
        """ Annual Report document links """
        self.cursor.execute(DOCUMENT_LINKS_ANNUAL_REPORT_GET)
        return self.cursor.fetchall()

    def document_links_unparsed_get(self) -> list:
        """ Find all unparsed document links """
        self.cursor.execute(DOCUMENT_LINK_RAWS_NOT_PARSED)
        return self.cursor.fetchall()

    def _filer_add(self, filer) -> Any:
        """ Add filer to storage
        Args:
            filer: tuple - name_first, name_last
        """
        self.cursor.execute(FILER_CREATE, filer)
        self.save()
        return self.cursor.lastrowid

    def _filers_get(self) -> list:
        """ Select all filers """
        self.cursor.execute(FILERS_READ)
        return self.cursor.fetchall()

    def _filers_set_cache(self) -> None:
        """ Fill filer cache """
        filers = self._filers_get()
        self._filers_by_name = {}
        for filer in filers:
            filer_name_key = f'{filer[1]}+|+{filer[2]}'
            self._filers_by_name[filer_name_key] = filer[0]

    def filer_get_key(self, name_first: str, name_last: str) -> int:
        """ Find or add filer """
        if not self._filers_by_name:
            self._filers_set_cache()

        first = name_first.lower()
        last = name_last.lower()
        filer_name_key = f'{first}+|+{last}'
        if filer_name_key not in self._filers_by_name:
            filer_key = self._filer_add((first, last))
            self._filers_by_name[filer_name_key] = filer_key

        return self._filers_by_name[filer_name_key]

    def _filer_types_get(self) -> list:
        """ Select all filer_types """
        self.cursor.execute(FILER_TYPES_READ)
        return self.cursor.fetchall()

    def filer_type_by_name(self, filer_type_name: str) -> int:
        """ Fetch and cache by name """
        if not self._filer_types_by_name:
            filer_types = self._filer_types_get()
            for filer_type in filer_types:
                key = filer_type[0]
                name = filer_type[1].lower()
                self._filer_types_by_name[name] = key

        return self._filer_types_by_name[filer_type_name]

    def document_link_raw_add(self, report) -> None:
        """ Add raw document links
        Args:
            report: tuple or list(tuple) - report_hash, name_first,
                name_last, filer_type, report_type, filed_date
        """
        command = self.cursor.executemany if isinstance(report, list) else self.cursor.execute
        command(DOCUMENT_LINK_RAW_CREATE, report)
        self.save()

    def document_link_raws_get(self) -> list:
        """ Select all document_link_raws """
        self.cursor.execute(DOCUMENT_LINK_RAWS_READ)
        return self.cursor.fetchall()
