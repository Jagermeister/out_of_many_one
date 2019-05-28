""" Constant SQL Statements """

### Report

REPORT_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report (
        report_key INTEGER PRIMARY KEY,
        report_hash TEXT,
        name_first TEXT,
        name_last TEXT,
        filer_type TEXT,
        report_type TEXT,
        filed_date TEXT
    );
'''

REPORT_CREATE = '''
    INSERT INTO report (
        report_hash,
        name_first,
        name_last,
        filer_type,
        report_type,
        filed_date
    ) VALUES (
        ?, ?, ?, ?, ?, ?
    )
'''

REPORTS_READ = '''
    SELECT
        report_key,
        report_hash,
        name_first,
        name_last,
        filer_type,
        report_type,
        filed_date
    FROM report AS R;
'''

TABLE_CREATIONS = [
    REPORT_TABLE_CREATE
]