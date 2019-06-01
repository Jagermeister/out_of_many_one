""" Constant SQL Statements """

### Report
# TODO: Update table name away from 'report'.
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


### Document Link

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

DOCUMENT_LINKS_ANNUAL_REPORT_GET = '''
    SELECT
        DL.document_link_key,
        DT.document_type_name,
        DL.is_paper,
        DL.unique_id
    FROM document_link AS DL
    JOIN document_type AS DT
        ON DT.document_type_key = DL.document_type_key
        AND DT.is_annual = 1
    WHERE DL.is_paper = 0;
'''


### Annual Report Raw
# TODO: Review if its safe to name 'Report_Annual' instead of with raw.

REPORT_ANNUAL_RAW_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_raw (
        report_annual_raw_key INTEGER PRIMARY KEY,
        document_link_key INTEGER NOT NULL,
        part_one_charity TEXT,
        part_two_earned_income TEXT,
        part_three_assets TEXT,
        part_four_a_ptr TEXT,
        part_four_b_transactions TEXT,
        part_five_gifts TEXT,
        part_six_travel TEXT,
        part_seven_liabilities TEXT,
        part_eight_positions TEXT,
        part_nine_agreements TEXT,
        part_ten_compensation TEXT,
        comments TEXT,
        FOREIGN KEY(document_link_key) REFERENCES document_link(document_link_key)
    );
'''

REPORT_ANNUAL_RAW_CREATE = '''
    INSERT INTO report_annual_raw (
        document_link_key,
        part_one_charity,
        part_two_earned_income,
        part_three_assets,
        part_four_a_ptr,
        part_four_b_transactions,
        part_five_gifts,
        part_six_travel,
        part_seven_liabilities,
        part_eight_positions,
        part_nine_agreements,
        part_ten_compensation,
        comments
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    );
'''

REPORT_ANNUALS_READ = '''
    SELECT
        A.report_annual_raw_key,
        A.document_link_key,
        A.part_one_charity,
        A.part_two_earned_income,
        A.part_three_assets,
        A.part_four_a_ptr,
        A.part_four_b_transactions,
        A.part_five_gifts,
        A.part_six_travel,
        A.part_seven_liabilities,
        A.part_eight_positions,
        A.part_nine_agreements,
        A.part_ten_compensation,
        A.comments
    FROM report_annual_raw AS A;
'''

### Annual Report Part One

REPORT_ANNUAL_CHARITY_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_charity (
        report_annual_charity_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        event_date INTEGER NOT NULL,
        activity TEXT NOT NULL,
        amount REAL NOT NULL,
        paid_person TEXT NOT NULL,
        paid_location TEXT NOT NULL,
        payment_received_person TEXT NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_CHARITY_CREATE = '''
    INSERT INTO report_annual_charity (
        report_annual_raw_key,
        event_id,
        event_date,
        activity,
        amount,
        paid_person,
        paid_location,
        payment_received_person
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?
    );
'''

### Annual Report Part Two

REPORT_ANNUAL_EARNED_INCOME_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_earned_income (
        report_annual_earned_income_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        payment_received_person TEXT NOT NULL,
        payment_type TEXT NOT NULL,
        paid_person TEXT NOT NULL,
        paid_location TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_EARNED_INCOME_CREATE = '''
    INSERT INTO report_annual_earned_income (
        report_annual_raw_key,
        event_id,
        payment_received_person,
        payment_type,
        paid_person,
        paid_location,
        amount
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?
    );
'''

### Annual Report Part Three

REPORT_ANNUAL_ASSET_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_asset (
        report_annual_asset_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id REAL NOT NULL,
        asset TEXT NOT NULL,
        asset_type TEXT NOT NULL,
        owner TEXT NOT NULL,
        value TEXT NOT NULL,
        income_type TEXT NOT NULL,
        income TEXT NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_ASSET_CREATE = '''
    INSERT INTO report_annual_asset (
        report_annual_raw_key,
        event_id,
        asset,
        asset_type,
        owner,
        value,
        income_type,
        income
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?
    )
'''

### Annual Report Four A

REPORT_ANNUAL_PTR_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_ptr (
        report_annual_ptr_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        transaction_date INTEGER NOT NULL,
        owner TEXT NOT NULL,
        ticker TEXT NOT NULL,
        asset TEXT NOT NULL,
        transaction_type TEXT NOT NULL,
        amount TEXT NOT NULL,
        comment TEXT,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_PTR_CREATE = '''
    INSERT INTO report_annual_ptr (
        report_annual_raw_key,
        event_id,
        transaction_date,
        owner,
        ticker,
        asset,
        transaction_type,
        amount,
        comment
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
'''

### Annual Report Four B

REPORT_ANNUAL_TRANSACTION_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_transaction (
        report_annual_transaction_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        owner TEXT NOT NULL,
        ticker TEXT NOT NULL,
        asset TEXT NOT NULL,
        transaction_type TEXT NOT NULL,
        transaction_date INTEGER NOT NULL,
        amount TEXT NOT NULL,
        comment TEXT,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_TRANSACTION_CREATE = '''
    INSERT INTO report_annual_transaction (
        report_annual_raw_key,
        event_id,
        owner,
        ticker,
        asset,
        transaction_type,
        transaction_date,
        amount,
        comment
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
'''

### Annual Report Six

REPORT_ANNUAL_TRAVEL_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_travel (
        report_annual_travel_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        travel_dates TEXT NOT NULL,
        travelers TEXT NOT NULL,
        travel_type TEXT NOT NULL,
        itinerary TEXT NOT NULL,
        reimbursed_for TEXT NOT NULL,
        paid_person TEXT NOT NULL,
        paid_location TEXT NOT NULL,
        comment TEXT NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_TRAVEL_CREATE = '''
    INSERT INTO report_annual_travel (
        report_annual_raw_key,
        event_id,
        travel_dates,
        travelers,
        travel_type,
        itinerary,
        reimbursed_for,
        paid_person,
        paid_location,
        comment
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
'''

### Annual Report Eight

REPORT_ANNUAL_POSITION_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_position (
        report_annual_position_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        position_dates TEXT NOT NULL,
        position TEXT NOT NULL,
        entity_name TEXT NOT NULL,
        entity_location TEXT NOT NULL,
        entity_type TEXT NOT NULL,
        comment TEXT,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_POSITION_CREATE = '''
    INSERT INTO report_annual_position (
        report_annual_raw_key,
        event_id,
        position_dates,
        position,
        entity_name,
        entity_location,
        entity_type,
        comment
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?
    )
'''

### Annual Report Nine

REPORT_ANNUAL_AGREEMENT_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_agreement (
        report_annual_agreement_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        agreement_date TEXT NOT NULL,
        party_name TEXT NOT NULL,
        party_location TEXT NOT NULL,
        agreement_type TEXT NOT NULL,
        status_and_terms TEXT NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_AGREEMENT_CREATE = '''
    INSERT INTO report_annual_agreement (
        report_annual_raw_key,
        event_id,
        agreement_date,
        party_name,
        party_location,
        agreement_type,
        status_and_terms
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?
    )
'''


TABLES_CREATION = [
    REPORT_ANNUAL_RAW_TABLE_CREATE,
    REPORT_ANNUAL_CHARITY_TABLE_CREATE,
    REPORT_ANNUAL_EARNED_INCOME_TABLE_CREATE,
    REPORT_ANNUAL_ASSET_TABLE_CREATE,
    REPORT_ANNUAL_PTR_TABLE_CREATE,
    REPORT_ANNUAL_TRANSACTION_TABLE_CREATE,
    REPORT_ANNUAL_TRAVEL_TABLE_CREATE,
    REPORT_ANNUAL_POSITION_TABLE_CREATE,
    REPORT_ANNUAL_AGREEMENT_TABLE_CREATE,
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
