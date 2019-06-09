# Parsing and Normalization

Continue to refine parsing of common values into side tables.

## Completed
- owner (Self, Spouse, Joint, Child)
- value/amount (Monetary ranges)
- transaction type (Sale, Purchase, Exchange)


## Table Column Distinct Value Counts
Low distinct value count relative to the total's row count could indicate a level of data duplication. Following metrics show row counts for each table along with column details on percentage of distinct values


**38029 `report_annual_asset`**
```c
[ ] 0.00     4 TEXT    owner
[ ] 0.00    13 TEXT    value
[ ] 0.00    53 TEXT    asset_type
[ ] 0.00   126 TEXT    income_type
[ ] 0.01   299 TEXT    income
[ ] 0.02   630 INTEGER report_annual_raw_key
[ ] 0.13  4847 TEXT    event_id
[ ] 0.25  9543 TEXT    asset
[ ] 1.00 38029 INTEGER report_annual_asset_key
```

**10817 `report_annual_transaction`**
```c
[ ] 0.00     4 TEXT    owner
[ ] 0.00     4 TEXT    transaction_type
[ ] 0.00     8 TEXT    amount
[ ] 0.03   312 INTEGER event_id
[ ] 0.04   382 INTEGER report_annual_raw_key
[ ] 0.04   483 TEXT    comment
[ ] 0.12  1253 TEXT    transaction_date
[ ] 0.12  1329 TEXT    ticker
[ ] 0.27  2893 TEXT    asset
[ ] 1.00 10817 INTEGER report_annual_transaction_key
```

**07506 `report_annual_ptr`**
```c
[ ] 0.00     4 TEXT    owner
[ ] 0.00     4 TEXT    transaction_type
[ ] 0.00     8 TEXT    amount
[ ] 0.02   158 TEXT    comment
[ ] 0.02   164 INTEGER report_annual_raw_key
[ ] 0.07   496 INTEGER event_id
[ ] 0.10   749 TEXT    ticker
[ ] 0.13   950 TEXT    transaction_date
[ ] 0.26  1940 TEXT    asset
[ ] 1.00  7506 INTEGER report_annual_ptr_key
```

**01518 `document_link`**
```c
[ ] 0.00     1 INTEGER is_paper
[ ] 0.00     2 INTEGER document_type_key
[ ] 0.00     3 INTEGER filer_type_key
[ ] 0.03    45 TEXT    document_name
[ ] 0.23   343 INTEGER filer_key
[ ] 0.37   555 TEXT    document_date
[ ] 1.00  1518 INTEGER document_link_key
[ ] 1.00  1518 INTEGER document_link_raw_key
[ ] 1.00  1518 TEXT    unique_id
```

**01518 `document_link_raw`**
```c
[ ] 0.00     3 TEXT    filer_type
[ ] 0.24   358 TEXT    name_last
[ ] 0.24   368 TEXT    name_first
[ ] 0.37   555 TEXT    filed_date
[ ] 1.00  1518 INTEGER document_link_raw_key
[ ] 1.00  1518 TEXT    document_link_raw_hash
[ ] 1.00  1518 TEXT    report_type
```

**01396 `report_annual_charity`**
```c
[ ] 0.00     3 TEXT    activity
[ ] 0.00     3 TEXT    payment_received_person
[ ] 0.07    98 INTEGER event_id
[ ] 0.08   109 INTEGER report_annual_raw_key
[ ] 0.11   157 REAL    amount
[ ] 0.18   256 TEXT    paid_location
[ ] 0.29   398 TEXT    event_date
[ ] 0.41   567 TEXT    paid_person
[ ] 1.00  1396 INTEGER report_annual_charity_key
```

**01303 `report_annual_liability`**
```c
[ ] 0.00     4 TEXT    debtor
[ ] 0.01     8 TEXT    amount
[ ] 0.01    13 TEXT    points
[ ] 0.01    18 INTEGER event_id
[ ] 0.02    25 INTEGER year_incurred
[ ] 0.02    31 TEXT    liability_type
[ ] 0.12   158 TEXT    creditor_location
[ ] 0.13   165 TEXT    comments
[ ] 0.14   178 TEXT    creditor_name
[ ] 0.21   277 TEXT    term_rate
[ ] 0.40   525 INTEGER report_annual_raw_key
[ ] 1.00  1303 INTEGER report_annual_liability_key
```

**01192 `report_annual_earned_income`**
```c
[ ] 0.00     2 TEXT    payment_received_person
[ ] 0.01    10 INTEGER event_id
[ ] 0.06    70 TEXT    payment_type
[ ] 0.15   178 TEXT    paid_location
[ ] 0.26   307 REAL    amount
[ ] 0.27   322 TEXT    paid_person
[ ] 0.41   488 INTEGER report_annual_raw_key
[ ] 1.00  1192 INTEGER report_annual_earned_income_key
```

**01101 `report_annual_position`**
```c
[ ] 0.02    26 INTEGER event_id
[ ] 0.04    40 TEXT    comment
[ ] 0.04    49 TEXT    entity_type
[ ] 0.07    79 TEXT    position
[ ] 0.11   121 TEXT    entity_location
[ ] 0.18   193 TEXT    position_dates
[ ] 0.22   244 TEXT    entity_name
[ ] 0.32   349 INTEGER report_annual_raw_key
[ ] 1.00  1101 INTEGER report_annual_position_key
```

**01052 `report_annual_raw`**
```c
[ ] 0.02    21 TEXT    part_five_gifts
[ ] 0.06    60 TEXT    part_six_travel
[ ] 0.10   108 TEXT    part_one_charity
[ ] 0.13   142 TEXT    comments
[ ] 0.14   147 TEXT    part_ten_compensation
[ ] 0.19   204 TEXT    part_four_a_ptr
[ ] 0.23   240 TEXT    part_nine_agreements
[ ] 0.32   339 TEXT    part_eight_positions
[ ] 0.41   429 TEXT    part_four_b_transactions
[ ] 0.42   445 TEXT    part_seven_liabilities
[ ] 0.50   530 TEXT    part_two_earned_income
[ ] 0.90   951 TEXT    part_three_assets
[ ] 1.00  1052 INTEGER report_annual_raw_key
[ ] 1.00  1052 INTEGER document_link_key
[ ] 1.00  1052 TEXT    header
```

**00649 `report_annual_agreement`**
```c
[ ] 0.01     8 INTEGER event_id
[ ] 0.03    22 TEXT    agreement_type
[ ] 0.12    80 TEXT    party_location
[ ] 0.14    94 TEXT    agreement_date
[ ] 0.19   124 TEXT    party_name
[ ] 0.31   201 TEXT    status_and_terms
[ ] 0.47   302 INTEGER report_annual_raw_key
[ ] 1.00   649 INTEGER report_annual_agreement_key
```

**00630 `report_annual`**
```c
[ ] 0.00     0 INTEGER calendar_year
[ ] 0.10    62 TEXT    comment
[ ] 0.17   106 TEXT    filer_name
[ ] 0.97   611 TEXT    filed_date
[ ] 1.00   630 INTEGER report_annual_key
[ ] 1.00   630 INTEGER report_annual_raw_key
```

**00343 `filer`**
```c
[ ] 0.78   268 TEXT    name_last
[ ] 0.87   298 TEXT    name_first
[ ] 1.00   343 INTEGER filer_key
```

**00289 `report_annual_compensation`**
```c
[ ] 0.12    34 INTEGER event_id
[ ] 0.17    48 TEXT    duties
[ ] 0.18    53 INTEGER report_annual_raw_key
[ ] 0.27    79 TEXT    source_location
[ ] 0.40   117 TEXT    source_name
[ ] 1.00   289 INTEGER report_annual_compensation_key
```

**00178 `report_annual_travel`**
```c
[ ] 0.02     4 TEXT    travelers
[ ] 0.04     7 TEXT    travel_type
[ ] 0.11    19 INTEGER event_id
[ ] 0.15    27 TEXT    comment
[ ] 0.18    32 TEXT    paid_location
[ ] 0.26    46 TEXT    paid_person
[ ] 0.42    75 INTEGER report_annual_raw_key
[ ] 0.48    85 TEXT    reimbursed_for
[ ] 0.62   111 TEXT    itinerary
[ ] 0.68   121 TEXT    travel_dates
[ ] 1.00   178 INTEGER report_annual_travel_key
```

**00053 `report_annual_attachment`**
```c
[ ] 0.57    30 INTEGER report_annual_raw_key
[ ] 0.74    39 TEXT    attachment_name
[ ] 0.79    42 TEXT    attached_date
[ ] 1.00    53 INTEGER report_annual_attachment_key
[ ] 1.00    53 TEXT    link
```

**00027 `report_annual_gift`**
```c
[ ] 0.07     2 TEXT    recipient
[ ] 0.22     6 INTEGER event_id
[ ] 0.41    11 TEXT    from_location
[ ] 0.56    15 INTEGER report_annual_raw_key
[ ] 0.70    19 TEXT    from_person
[ ] 0.78    21 TEXT    gift_date
[ ] 0.78    21 REAL    value
[ ] 0.89    24 TEXT    gift
[ ] 1.00    27 INTEGER report_annual_gift_key
```

**00006 `document_type`**
```c
[ ] 0.33     2 INTEGER is_annual
[ ] 0.33     2 INTEGER is_blind_trust
[ ] 0.33     2 INTEGER is_due_date_extension
[ ] 0.33     2 INTEGER is_miscellaneous_information
[ ] 0.33     2 INTEGER is_periodic_transaction_report
[ ] 0.33     2 INTEGER is_unknown
[ ] 1.00     6 INTEGER document_type_key
[ ] 1.00     6 TEXT    document_type_name
```

**00003 `filer_type`**
```c
[ ] 0.67     2 INTEGER is_senator
[ ] 0.67     2 INTEGER is_candidate
[ ] 0.67     2 INTEGER is_former_senator
[ ] 1.00     3 INTEGER filer_type_key
[ ] 1.00     3 TEXT    filer_name
```
