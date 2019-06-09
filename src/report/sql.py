""" Simple reporting basics """

from src.store.sql import TABLE_NAMES

count_query = '''
    SELECT
        '{0}',
        COUNT(*)
    FROM {0};
'''

def table_counts(cursor):
    """ Table names and their row counts """
    results = []
    for table in TABLE_NAMES:
        cursor.execute(count_query.format(table))
        results.extend(cursor.fetchall())

    return sorted(results, key=lambda r: r[1], reverse=True)

def column_distinct_values(cursor):
    table_column_query = '''
        pragma table_info({});
    '''
    distinct_values_query = '''
        SELECT
            '{0}',
            COUNT(DISTINCT T.{0})
        FROM {1} AS T;
    '''
    table_stats = []
    columns_by_table_name = {}
    for table in TABLE_NAMES:
        cursor.execute(table_column_query.format(table))
        columns = cursor.fetchall()
        cursor.execute(count_query.format(table))
        row_count = cursor.fetchall()[0][1]
        table_stats.append((table, row_count))
        results = []
        for column in columns:
            cursor.execute(distinct_values_query.format(
                column[1], table))
            result = list(cursor.fetchall()[0])
            result.extend([column[2]])
            results.append(tuple(result))

        results = sorted(results, key=lambda k: k[1])
        columns_by_table_name[table] = results

    table_stats = sorted(table_stats, key=lambda k: k[1], reverse=True)
    for table in table_stats:
        name, row_count = table
        print('**{:05} `{}`**'.format(row_count, name))
        column_stats = columns_by_table_name[name]
        print('```c')
        for column in column_stats:
            name, count, datatype = column
            print('[ ] {:.2f} {} {} {}'.format(
                count/row_count, str(count).rjust(5), datatype.ljust(7), name))

        print('```', end='\n\n')
