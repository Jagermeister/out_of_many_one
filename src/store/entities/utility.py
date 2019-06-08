""" Common methods for table creation, population, and reading """

import sqlite3

from src.store.config import DATABASE_NAME

__connection = None
__cursor = None

def _cursor_get():
    """ Fetch or create Sqlite cursor """
    global __connection, __cursor
    if not __cursor:
        __connection = sqlite3.connect(DATABASE_NAME)
        __cursor = __connection.cursor()

    return __cursor

def _save():
    """ Connection Commit """
    __connection.commit()

def _close():
    """ Connection Close """
    __connection.close()

def _table_create(table):
    """ Execute CREATE TABLE IF NOT EXISTS statement """
    cursor = _cursor_get()
    cursor.execute(table)
    _save()

def _table_populate(defaults, populate):
    """ Ensure table has defaults populated
    Args:
        defaults: list[dict] - Default values to insert
        populate: str - SQL Insert statement (with duplicate
            checking to ensure only one of each default)
    """
    cursor = _cursor_get()
    for default in defaults:
        cursor.execute(populate, default)
    
    _save()

def _table_read(read):
    """ Execute Select statment
    Args:
        read: str - SQL Select statement
    """
    cursor = _cursor_get()
    cursor.execute(read)
    results = cursor.fetchall()
    _close()
    return results


def fetch_table_values(table, defaults, populate, read):
    """ Handle Table Creation, Population, and Reading
    Args:
        table: str - SQL Table Create statement
        defaults: list[dict] - Default values to insert
        populate: str - SQL Insert statement (with duplicate
            checking to ensure only one of each default)
        read: str - SQL Select statement
    """
    _table_create(table)
    _table_populate(defaults, populate)
    return _table_read(read)
