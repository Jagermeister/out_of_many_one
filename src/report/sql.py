""" Simple reporting basics """

from src.store.sql import TABLE_NAMES

def table_counts(cursor):
    """ Table names and their row counts """
    count_query = '''
        SELECT
            "{0}",
            COUNT(*)
        FROM {0};
    '''
    results = []
    for table in TABLE_NAMES:
        cursor.execute(count_query.format(table))
        results.append(cursor.fetchall()[0])

    return sorted(results, key=lambda r: r[1], reverse=True)
