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
    );
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


### Filer

FILER_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS filer (
        filer_key INTEGER PRIMARY KEY,
        name_first TEXT NOT NULL,
        name_last TEXT NOT NULL
    );
'''


### Filer Type

FILER_TYPE_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS filer_type (
        filer_type_key INTEGER PRIMARY KEY,
        filer_name TEXT NOT NULL,
        is_senator INTEGER NOT NULL,
        is_candidate INTEGER NOT NULL,
        is_former_senator INTEGER NOT NULL
    );
'''


### Document Type

DOCUMENT_TYPE_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS document_type (
        document_type_key INTEGER PRIMARY KEY,
        document_type_name TEXT NOT NULL,
        is_electronic INTEGER NOT NULL,
        is_paper INTEGER NOT NULL
    );
'''


### Document

DOCUMENT_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS document (
        document_key INTEGER PRIMARY KEY,
        filer_key INTEGER NOT NULL,
        filter_type_key INTEGER NOT NULL,
        document_type_key INTEGER NOT NULL,
        unique_id TEXT NOT NULL,
        document_name TEXT,
        document_year INTEGER,
        document_date INTEGER,
        FOREIGN KEY(filer_key) REFERENCES filer(filer_key),
        FOREIGN KEY(filter_type_key) REFERENCES filer_type(filter_type_key),
        FOREIGN KEY(document_type_key) REFERENCES document_type(document_type_key)
    );
'''

TABLE_CREATIONS = [
    DOCUMENT_TABLE_CREATE,
    DOCUMENT_TYPE_TABLE_CREATE,
    FILER_TABLE_CREATE,
    FILER_TYPE_TABLE_CREATE,
    REPORT_TABLE_CREATE
]