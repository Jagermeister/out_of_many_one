# Parsing and Normalization

Continue to refine parsing of common values into side tables.

## report_annual_asset

0|report_annual_asset_key|INTEGER|0||1
1|report_annual_raw_key|INTEGER|1||0
2|event_id|TEXT|1||0
3|asset|TEXT|1||0
4|asset_type|TEXT|1||0
~~5|owner|TEXT|1||0
~~6|value|TEXT|1||0
7|income_type|TEXT|1||0
8|income|TEXT|1||0

## report_annual_transaction

0|report_annual_transaction_key|INTEGER|0||1
1|report_annual_raw_key|INTEGER|1||0
2|event_id|INTEGER|1||0
~~3|owner|TEXT|1||0
4|ticker|TEXT|1||0
5|asset|TEXT|1||0
6|transaction_type|TEXT|1||0
7|transaction_date|TEXT|1||0
~~8|amount|TEXT|1||0
9|comment|TEXT|0||0

### ticker
distinct: 1329

### transaction_type
Sale (Partial)
Purchase
Sale (Full)
Exchange
