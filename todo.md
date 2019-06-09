# Parsing and Normalization

Continue to refine parsing of common values into side tables.

## Completed
- owner (Self, Spouse, Joint, Child)
- value/amount (Monetary ranges)
- transaction type (Sale, Purchase, Exchange)


## Table Column Distinct Value Counts
Low distinct value count relative to the total's row count could indicate a level of data duplication. Following metrics show row counts for each table along with column details on percentage of distinct values

| |Description|
|---|---|
|x|No data duplication requiring normalization|
|>|Key table available for use|
|!|Additional parsing required|
|R|Raw table which stores data as captured|

**38029 `report_annual_asset`**
```c
[>] 0.00     4 TEXT    owner  --> asset_owner
[>] 0.00    13 TEXT    value  --> dollar_value
[!] 0.00    53 TEXT    asset_type
   'Needs to be parsed into major type (Life Insurance, Real Estate, etc)
    and minor type (Variable, Commercial, etc)' 
[!] 0.00   126 TEXT    income_type
   'Needs to be parsed from comma separated list (Dividends, Interest,
    Other, None, etc) to a one-to-many table. Need to add income_type_comment'
[!] 0.01   299 TEXT    income
   'Needs to be parsed into dollar_value key and other value REAL'
[x] 0.02   630 INTEGER report_annual_raw_key
[x] 0.13  4847 TEXT    event_id
[!] 0.25  9543 TEXT    asset
   'Much noise to clean up to parse the data from the formatting'
[x] 1.00 38029 INTEGER report_annual_asset_key
```

**10817 `report_annual_transaction`**
```c
[>] 0.00     4 TEXT    owner  --> asset_owner
[>] 0.00     4 TEXT    transaction_type  --> transaction_type
[>] 0.00     8 TEXT    amount  --> dollar_value
[x] 0.03   312 INTEGER event_id
[x] 0.04   382 INTEGER report_annual_raw_key
[!] 0.04   483 TEXT    comment
   'Diverse set of data contained depending on the transaction
    type. Further data review needed before next steps'
[x] 0.12  1253 TEXT    transaction_date
[!] 0.12  1329 TEXT    ticker
   'Remove yahoo finance links'
[!] 0.27  2893 TEXT    asset
   'Advanced project to map ticker to asset characteristics'
[x] 1.00 10817 INTEGER report_annual_transaction_key
```

**07506 `report_annual_ptr`**
```c
[>] 0.00     4 TEXT    owner  --> asset_owner
[>] 0.00     4 TEXT    transaction_type  --> transaction_type
[>] 0.00     8 TEXT    amount  --> dollar_value
[!] 0.02   158 TEXT    comment
   'Lowest priority - many comments could be reduced, but no
    added value provided in most cases'
[x] 0.02   164 INTEGER report_annual_raw_key
[x] 0.07   496 INTEGER event_id
[!] 0.10   749 TEXT    ticker
   'Advanced project to map ticker to asset characteristics'
[x] 0.13   950 TEXT    transaction_date
[!] 0.26  1940 TEXT    asset
   'Several asset types which have unique data embedded.
    Advanced project to map ticker to asset characteristics'
[x] 1.00  7506 INTEGER report_annual_ptr_key
```

**01518 `document_link`**
```c
[x] 0.00     1 INTEGER is_paper
[x] 0.00     2 INTEGER document_type_key
[x] 0.00     3 INTEGER filer_type_key
[!] 0.03    45 TEXT    document_name
   'Looks like report_type_name, report_year, and optional
    amendment revision available to be parsed'
[x] 0.23   343 INTEGER filer_key
[x] 0.37   555 TEXT    document_date
[x] 1.00  1518 INTEGER document_link_key
[x] 1.00  1518 INTEGER document_link_raw_key
[x] 1.00  1518 TEXT    unique_id
```

**01518 `document_link_raw`**
```c
[R] 0.00     3 TEXT    filer_type
[R] 0.24   358 TEXT    name_last
[R] 0.24   368 TEXT    name_first
[R] 0.37   555 TEXT    filed_date
[x] 1.00  1518 INTEGER document_link_raw_key
[x] 1.00  1518 TEXT    document_link_raw_hash
[R] 1.00  1518 TEXT    report_type
```

**01396 `report_annual_charity`**
```c
[ ] 0.00     3 TEXT    activity
[ ] 0.00     3 TEXT    payment_received_person
[x] 0.07    98 INTEGER event_id
[x] 0.08   109 INTEGER report_annual_raw_key
[ ] 0.11   157 REAL    amount
[ ] 0.18   256 TEXT    paid_location
[ ] 0.29   398 TEXT    event_date
[ ] 0.41   567 TEXT    paid_person
[x] 1.00  1396 INTEGER report_annual_charity_key
```

**01303 `report_annual_liability`**
```c
[ ] 0.00     4 TEXT    debtor
[ ] 0.01     8 TEXT    amount
[ ] 0.01    13 TEXT    points
[x] 0.01    18 INTEGER event_id
[ ] 0.02    25 INTEGER year_incurred
[ ] 0.02    31 TEXT    liability_type
[ ] 0.12   158 TEXT    creditor_location
[ ] 0.13   165 TEXT    comments
[ ] 0.14   178 TEXT    creditor_name
[ ] 0.21   277 TEXT    term_rate
[x] 0.40   525 INTEGER report_annual_raw_key
[x] 1.00  1303 INTEGER report_annual_liability_key
```

**01192 `report_annual_earned_income`**
```c
[ ] 0.00     2 TEXT    payment_received_person
[x] 0.01    10 INTEGER event_id
[ ] 0.06    70 TEXT    payment_type
[ ] 0.15   178 TEXT    paid_location
[ ] 0.26   307 REAL    amount
[ ] 0.27   322 TEXT    paid_person
[x] 0.41   488 INTEGER report_annual_raw_key
[x] 1.00  1192 INTEGER report_annual_earned_income_key
```

**01101 `report_annual_position`**
```c
[x] 0.02    26 INTEGER event_id
[ ] 0.04    40 TEXT    comment
[ ] 0.04    49 TEXT    entity_type
[ ] 0.07    79 TEXT    position
[ ] 0.11   121 TEXT    entity_location
[ ] 0.18   193 TEXT    position_dates
[ ] 0.22   244 TEXT    entity_name
[x] 0.32   349 INTEGER report_annual_raw_key
[x] 1.00  1101 INTEGER report_annual_position_key
```

**01052 `report_annual_raw`**
```c
[R] 0.02    21 TEXT    part_five_gifts
[R] 0.06    60 TEXT    part_six_travel
[R] 0.10   108 TEXT    part_one_charity
[R] 0.13   142 TEXT    comments
[R] 0.14   147 TEXT    part_ten_compensation
[R] 0.19   204 TEXT    part_four_a_ptr
[R] 0.23   240 TEXT    part_nine_agreements
[R] 0.32   339 TEXT    part_eight_positions
[R] 0.41   429 TEXT    part_four_b_transactions
[R] 0.42   445 TEXT    part_seven_liabilities
[R] 0.50   530 TEXT    part_two_earned_income
[R] 0.90   951 TEXT    part_three_assets
[x] 1.00  1052 INTEGER report_annual_raw_key
[x] 1.00  1052 INTEGER document_link_key
[R] 1.00  1052 TEXT    header
```

**00649 `report_annual_agreement`**
```c
[x] 0.01     8 INTEGER event_id
[ ] 0.03    22 TEXT    agreement_type
[ ] 0.12    80 TEXT    party_location
[ ] 0.14    94 TEXT    agreement_date
[ ] 0.19   124 TEXT    party_name
[ ] 0.31   201 TEXT    status_and_terms
[x] 0.47   302 INTEGER report_annual_raw_key
[x] 1.00   649 INTEGER report_annual_agreement_key
```

**00630 `report_annual`**
```c
[ ] 0.00     0 INTEGER calendar_year
[ ] 0.10    62 TEXT    comment
[ ] 0.17   106 TEXT    filer_name
[ ] 0.97   611 TEXT    filed_date
[x] 1.00   630 INTEGER report_annual_key
[x] 1.00   630 INTEGER report_annual_raw_key
```

**00343 `filer`**
```c
[x] 0.78   268 TEXT    name_last
[x] 0.87   298 TEXT    name_first
[x] 1.00   343 INTEGER filer_key
```

**00289 `report_annual_compensation`**
```c
[x] 0.12    34 INTEGER event_id
[ ] 0.17    48 TEXT    duties
[x] 0.18    53 INTEGER report_annual_raw_key
[ ] 0.27    79 TEXT    source_location
[ ] 0.40   117 TEXT    source_name
[x] 1.00   289 INTEGER report_annual_compensation_key
```

**00178 `report_annual_travel`**
```c
[ ] 0.02     4 TEXT    travelers
[ ] 0.04     7 TEXT    travel_type
[x] 0.11    19 INTEGER event_id
[ ] 0.15    27 TEXT    comment
[ ] 0.18    32 TEXT    paid_location
[ ] 0.26    46 TEXT    paid_person
[x] 0.42    75 INTEGER report_annual_raw_key
[ ] 0.48    85 TEXT    reimbursed_for
[ ] 0.62   111 TEXT    itinerary
[ ] 0.68   121 TEXT    travel_dates
[x] 1.00   178 INTEGER report_annual_travel_key
```

**00053 `report_annual_attachment`**
```c
[x] 0.57    30 INTEGER report_annual_raw_key
[ ] 0.74    39 TEXT    attachment_name
[ ] 0.79    42 TEXT    attached_date
[x] 1.00    53 INTEGER report_annual_attachment_key
[ ] 1.00    53 TEXT    link
```

**00027 `report_annual_gift`**
```c
[ ] 0.07     2 TEXT    recipient
[x] 0.22     6 INTEGER event_id
[ ] 0.41    11 TEXT    from_location
[x] 0.56    15 INTEGER report_annual_raw_key
[ ] 0.70    19 TEXT    from_person
[ ] 0.78    21 TEXT    gift_date
[ ] 0.78    21 REAL    value
[ ] 0.89    24 TEXT    gift
[x] 1.00    27 INTEGER report_annual_gift_key
```

**00006 `document_type`**
```c
[x] 0.33     2 INTEGER is_annual
[x] 0.33     2 INTEGER is_blind_trust
[x] 0.33     2 INTEGER is_due_date_extension
[x] 0.33     2 INTEGER is_miscellaneous_information
[x] 0.33     2 INTEGER is_periodic_transaction_report
[x] 0.33     2 INTEGER is_unknown
[x] 1.00     6 INTEGER document_type_key
[x] 1.00     6 TEXT    document_type_name
```

**00003 `filer_type`**
```c
[x] 0.67     2 INTEGER is_senator
[x] 0.67     2 INTEGER is_candidate
[x] 0.67     2 INTEGER is_former_senator
[x] 1.00     3 INTEGER filer_type_key
[x] 1.00     3 TEXT    filer_name
```
