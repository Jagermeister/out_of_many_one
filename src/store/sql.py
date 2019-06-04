""" Constant SQL Statements """

### Document Link Raw

DOCUMENT_LINK_RAW_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS document_link_raw (
        document_link_raw_key INTEGER PRIMARY KEY,
        document_link_raw_hash TEXT,
        name_first TEXT,
        name_last TEXT,
        filer_type TEXT,
        report_type TEXT,
        filed_date TEXT
    );
'''

DOCUMENT_LINK_RAW_CREATE = '''
    INSERT INTO document_link_raw (
        document_link_raw_hash,
        name_first,
        name_last,
        filer_type,
        report_type,
        filed_date
    ) VALUES (
        ?, ?, ?, ?, ?, ?
    );
'''

DOCUMENT_LINK_RAWS_READ = '''
    SELECT
        document_link_raw_key,
        document_link_raw_hash,
        name_first,
        name_last,
        filer_type,
        report_type,
        filed_date
    FROM document_link_raw AS R;
'''

DOCUMENT_LINK_RAWS_NOT_PARSED = '''
    SELECT
        document_link_raw_key,
        name_first,
        name_last,
        filer_type,
        report_type,
        filed_date
    FROM document_link_raw AS R
    WHERE NOT EXISTS(
        SELECT *
        FROM document_link AS D
        WHERE D.document_link_raw_key = R.document_link_raw_key
    );
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

FILER_TYPE_DEFAULTS = [
    {'filer_name': 'Senator', 'is_senator': 1, 'is_candidate': 0, 'is_former_senator': 0},
    {'filer_name': 'Candidate', 'is_senator': 0, 'is_candidate': 1, 'is_former_senator': 0},
    {'filer_name': 'Former Senator', 'is_senator': 0, 'is_candidate': 0, 'is_former_senator': 1},
]

FILER_TYPE_POPULATE = '''
    INSERT INTO filer_type (
        filer_name,
        is_senator,
        is_candidate,
        is_former_senator
    )
    SELECT
        :filer_name, :is_senator, :is_candidate, :is_former_senator
    WHERE NOT EXISTS (
        SELECT *
        FROM filer_type AS FT
        WHERE FT.filer_name = :filer_name
            AND FT.is_senator = :is_senator
            AND FT.is_candidate = :is_candidate
            AND FT.is_former_senator = :is_former_senator
    );
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

DOCUMENT_TYPE_DEFAULTS = [
    {'document_type_name': 'Annual', 'is_annual': 1, 'is_blind_trust': 0, 'is_due_date_extension': 0, 'is_miscellaneous_information': 0, 'is_periodic_transaction_report': 0, 'is_unknown': 0},
    {'document_type_name': 'Blind Trusts', 'is_annual': 0, 'is_blind_trust': 1, 'is_due_date_extension': 0, 'is_miscellaneous_information': 0, 'is_periodic_transaction_report': 0, 'is_unknown': 0},
    {'document_type_name': 'Due Date Extension', 'is_annual': 0, 'is_blind_trust': 0, 'is_due_date_extension': 1, 'is_miscellaneous_information': 0, 'is_periodic_transaction_report': 0, 'is_unknown': 0},
    {'document_type_name': 'Miscellaneous Information', 'is_annual': 0, 'is_blind_trust': 0, 'is_due_date_extension': 0, 'is_miscellaneous_information': 1, 'is_periodic_transaction_report': 0, 'is_unknown': 0},
    {'document_type_name': 'Periodic Transaction Report', 'is_annual': 0, 'is_blind_trust': 0, 'is_due_date_extension': 0, 'is_miscellaneous_information': 0, 'is_periodic_transaction_report': 1, 'is_unknown': 0},
    {'document_type_name': 'UNKNOWN', 'is_annual': 0, 'is_blind_trust': 0, 'is_due_date_extension': 0, 'is_miscellaneous_information': 0, 'is_periodic_transaction_report': 0, 'is_unknown': 1},
]

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
    SELECT
        :document_type_name,
        :is_annual,
        :is_blind_trust,
        :is_due_date_extension,
        :is_miscellaneous_information,
        :is_periodic_transaction_report,
        :is_unknown
    WHERE NOT EXISTS (
        SELECT *
        FROM document_type AS DT
        WHERE DT.document_type_name = :document_type_name
            AND DT.is_annual = :is_annual
            AND DT.is_blind_trust = :is_blind_trust
            AND DT.is_due_date_extension = :is_due_date_extension
            AND DT.is_miscellaneous_information = :is_miscellaneous_information
            AND DT.is_periodic_transaction_report = :is_periodic_transaction_report
            AND DT.is_unknown = :is_unknown
    );
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
        document_link_raw_key INTEGER NOT NULL,
        filer_key INTEGER NOT NULL,
        filer_type_key INTEGER NOT NULL,
        document_type_key INTEGER NOT NULL,
        is_paper INTEGER NOT NULL,
        unique_id TEXT NOT NULL,
        document_name TEXT,
        document_date TEXT,
        FOREIGN KEY(document_link_raw_key) REFERENCES document_link_raw(document_link_raw_key),
        FOREIGN KEY(filer_key) REFERENCES filer(filer_key),
        FOREIGN KEY(filer_type_key) REFERENCES filer_type(filer_type_key),
        FOREIGN KEY(document_type_key) REFERENCES document_type(document_type_key)
    );
'''

DOCUMENT_LINK_CREATE = '''
    INSERT INTO document_link (
        document_link_raw_key,
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
        DL.unique_id
    FROM document_link AS DL
    JOIN document_type AS DT
        ON DT.document_type_key = DL.document_type_key
        AND DT.is_annual = 1
    WHERE DL.is_paper = 0
        AND NOT EXISTS (
            SELECT *
            FROM report_annual_raw AS R
            WHERE R.document_link_key = DL.document_link_key
        )
'''

### Annual Report Raw

REPORT_ANNUAL_RAW_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_raw (
        report_annual_raw_key INTEGER PRIMARY KEY,
        document_link_key INTEGER NOT NULL,
        header TEXT,
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
        header,
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
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    );
'''

REPORT_ANNUALS_READ = '''
    SELECT
        R.report_annual_raw_key,
        R.document_link_key,
        R.header,
        R.part_one_charity,
        R.part_two_earned_income,
        R.part_three_assets,
        R.part_four_a_ptr,
        R.part_four_b_transactions,
        R.part_five_gifts,
        R.part_six_travel,
        R.part_seven_liabilities,
        R.part_eight_positions,
        R.part_nine_agreements,
        R.part_ten_compensation,
        R.comments
    FROM report_annual_raw AS R
    JOIN document_link AS D
        ON D.document_link_key = R.document_link_key
    JOIN filer_type AS F
        ON F.filer_type_key = D.filer_type_key
        AND F.is_senator = 1
    WHERE NOT EXISTS (
        SELECT *
        FROM report_annual AS A
        WHERE A.report_annual_raw_key = R.report_annual_raw_key
    )
'''

### Annual Report

REPORT_ANNUAL_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual (
        report_annual_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        calendar_year INTEGER NOT NULL,
        filer_name TEXT NOT NULL,
        filed_date TEXT NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

### Annual Report Part One

REPORT_ANNUAL_CHARITY_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_charity (
        report_annual_charity_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        event_date TEXT NOT NULL,
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
        transaction_date TEXT NOT NULL,
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
        transaction_date TEXT NOT NULL,
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

### Annual Report Five

REPORT_ANNUAL_GIFT_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_gift (
        report_annual_gift_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        gift_date TEXT NOT NULL,
        recipient TEXT NOT NULL,
        gift TEXT NOT NULL,
        value REAL NOT NULL,
        from_person TEXT NOT NULL,
        from_location TEXT NOT NULL,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_GIFT_CREATE = '''
    INSERT INTO report_annual_gift (
        report_annual_raw_key,
        event_id,
        gift_date,
        recipient,
        gift,
        value,
        from_person,
        from_location
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?
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

### Annual Report Seven

REPORT_ANNUAL_LIABILITY_TABLE_CREATE = '''
    CREATE TABLE IF NOT EXISTS report_annual_liability (
        report_annual_liability_key INTEGER PRIMARY KEY,
        report_annual_raw_key INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        year_incurred INTEGER NOT NULL,
        debtor TEXT NOT NULL,
        liability_type TEXT NOT NULL,
        points TEXT NOT NULL,
        term_rate TEXT NOT NULL,
        amount TEXT NOT NULL,
        creditor_name TEXT NOT NULL,
        creditor_location TEXT NOT NULL,
        comments TEXT,
        FOREIGN KEY(report_annual_raw_key) REFERENCES report_annual_raw(report_annual_raw_key)
    );
'''

REPORT_ANNUAL_LIABILITY_CREATE = '''
    INSERT INTO report_annual_liability (
        report_annual_raw_key,
        event_id,
        year_incurred,
        debtor,
        liability_type,
        points,
        term_rate,
        amount,
        creditor_name,
        creditor_location,
        comments
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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

### Index and table creation

TABLE_INDEXES_CREATION = """
    CREATE INDEX IF NOT EXISTS 'document_link_document_type_key' ON 'document_link'('document_type_key');
    CREATE INDEX IF NOT EXISTS 'document_link_filer_type_key' ON 'document_link'('filer_type_key');
    CREATE INDEX IF NOT EXISTS 'document_link_filer_key' ON 'document_link'('filer_key');
    CREATE INDEX IF NOT EXISTS 'document_link_document_link_raw_key' ON 'document_link'('document_link_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_raw_document_link_key' ON 'report_annual_raw'('document_link_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_agreement_report_annual_raw_key' ON 'report_annual_agreement'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_asset_report_annual_raw_key' ON 'report_annual_asset'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_charity_report_annual_raw_key' ON 'report_annual_charity'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_earned_income_report_annual_raw_key' ON 'report_annual_earned_income'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_gift_report_annual_raw_key' ON 'report_annual_gift'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_liability_report_annual_raw_key' ON 'report_annual_liability'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_position_report_annual_raw_key' ON 'report_annual_position'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_ptr_report_annual_raw_key' ON 'report_annual_ptr'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_transaction_report_annual_raw_key' ON 'report_annual_transaction'('report_annual_raw_key');
    CREATE INDEX IF NOT EXISTS 'report_annual_travel_report_annual_raw_key' ON 'report_annual_travel'('report_annual_raw_key');
"""

TABLES_CREATION = [
    REPORT_ANNUAL_RAW_TABLE_CREATE,
    REPORT_ANNUAL_TABLE_CREATE,
    REPORT_ANNUAL_CHARITY_TABLE_CREATE,
    REPORT_ANNUAL_EARNED_INCOME_TABLE_CREATE,
    REPORT_ANNUAL_ASSET_TABLE_CREATE,
    REPORT_ANNUAL_PTR_TABLE_CREATE,
    REPORT_ANNUAL_TRANSACTION_TABLE_CREATE,
    REPORT_ANNUAL_GIFT_TABLE_CREATE,
    REPORT_ANNUAL_TRAVEL_TABLE_CREATE,
    REPORT_ANNUAL_LIABILITY_TABLE_CREATE,
    REPORT_ANNUAL_POSITION_TABLE_CREATE,
    REPORT_ANNUAL_AGREEMENT_TABLE_CREATE,
    DOCUMENT_LINK_TABLE_CREATE,
    DOCUMENT_TYPE_TABLE_CREATE,
    FILER_TABLE_CREATE,
    FILER_TYPE_TABLE_CREATE,
    DOCUMENT_LINK_RAW_TABLE_CREATE
]
