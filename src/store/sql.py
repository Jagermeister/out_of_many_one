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

FILER_CREATE = '''
    INSERT INTO filer (
        name_first,
        name_last
    ) VALUES (
        ?, ?
    );
'''

FILERS_READ = '''
    SELECT
        F.filer_key,
        F.name_first,
        F.name_last
    FROM filer AS F;
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

FILER_TYPES_READ = '''
    SELECT
        FT.filer_type_key,
        FT.filer_name,
        FT.is_senator,
        FT.is_candidate,
        FT.is_former_senator
    FROM filer_type AS FT;
'''

FILTER_TYPE_POPULATE = '''
    INSERT INTO filer_type (
        filer_name,
        is_senator,
        is_candidate,
        is_former_senator
    )
    VALUES
        ('Senator', 1, 0, 0),
        ('Candidate', 0, 1, 0),
        ('Former Senator', 0, 0, 1);
'''


### Document Type

DOCUMENT_TYPE_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS document_type (
        document_type_key INTEGER PRIMARY KEY,
        document_type_name TEXT NOT NULL,
        is_annual INTEGER NOT NULL,
        is_blind_trust INTEGER NOT NULL,
        is_due_date_extension INTEGER NOT NULL,
        is_miscellaneous_information INTEGER NOT NULL,
        is_periodic_transaction_report INTEGER NOT NULL,
        is_unknown INTEGER NOT NULL
    );
'''

DOCUMENT_TYPE_POPULATE = '''
    INSERT INTO document_type (
        document_type_name,
        is_annual,
        is_blind_trust,
        is_due_date_extension,
        is_miscellaneous_information,
        is_periodic_transaction_report,
        is_unknown
    )
    VALUES
        ('Annual', 1, 0, 0, 0, 0, 0),
        ('Blind Trusts', 0, 1, 0, 0, 0, 0),
        ('Due Date Extension', 0, 0, 1, 0, 0, 0),
        ('Miscellaneous Information', 0, 0, 0, 1, 0, 0),
        ('Periodic Transaction Report', 0, 0, 0, 0, 1, 0),
        ('UNKNOWN', 0, 0, 0, 0, 0, 1);
'''

DOCUMENT_TYPES_READ = '''
    SELECT
        DT.document_type_key,
        DT.document_type_name,
        DT.is_annual,
        DT.is_blind_trust,
        DT.is_due_date_extension,
        DT.is_miscellaneous_information,
        DT.is_periodic_transaction_report,
        DT.is_unknown
    FROM document_type AS DT;
'''


### Document

DOCUMENT_LINK_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS document_link (
        document_link_key INTEGER PRIMARY KEY,
        report_key INTEGER NOT NULL,
        filer_key INTEGER NOT NULL,
        filer_type_key INTEGER NOT NULL,
        document_type_key INTEGER NOT NULL,
        is_paper INTEGER NOT NULL,
        unique_id TEXT NOT NULL,
        document_name TEXT,
        document_date INTEGER,
        FOREIGN KEY(report_key) REFERENCES report(report_key),
        FOREIGN KEY(filer_key) REFERENCES filer(filer_key),
        FOREIGN KEY(filer_type_key) REFERENCES filer_type(filer_type_key),
        FOREIGN KEY(document_type_key) REFERENCES document_type(document_type_key)
    );
'''

DOCUMENT_LINK_CREATE = '''
    INSERT INTO document_link (
        report_key,
        filer_key,
        filer_type_key,
        document_type_key,
        is_paper,
        unique_id,
        document_name,
        document_date
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?
    )
'''


TABLES_CREATION = [
    DOCUMENT_LINK_TABLE_CREATE,
    DOCUMENT_TYPE_TABLE_CREATE,
    FILER_TABLE_CREATE,
    FILER_TYPE_TABLE_CREATE,
    REPORT_TABLE_CREATE
]

TABLES_POPULATE_DATA = [
    DOCUMENT_TYPE_POPULATE,
    FILTER_TYPE_POPULATE
]