# Parsing and Normalization

Continue to refine parsing of common values into side tables.


## report_annual_asset

0|report_annual_asset_key|INTEGER|0||1
1|report_annual_raw_key|INTEGER|1||0
2|event_id|TEXT|1||0
3|asset|TEXT|1||0
4|asset_type|TEXT|1||0
5|owner|TEXT|1||0
6|value|TEXT|1||0
7|income_type|TEXT|1||0
8|income|TEXT|1||0

### owner
Joint
Self
Spouse
Child

### value
$50,001 - $100,000
$15,001 - $50,000
$1,001 - $15,000

Unascertainable
$250,001 - $500,000
$100,001 - $250,000
None (or less than $1,001)
$1,000,001 - $5,000,000
$500,001 - $1,000,000
Over $1,000,000 and held independently by spouse or dependent child
$5,000,001 - $25,000,000
$25,000,001 - $50,000,000


## report_annual_transaction

0|report_annual_transaction_key|INTEGER|0||1
1|report_annual_raw_key|INTEGER|1||0
2|event_id|INTEGER|1||0
3|owner|TEXT|1||0
4|ticker|TEXT|1||0
5|asset|TEXT|1||0
6|transaction_type|TEXT|1||0
7|transaction_date|TEXT|1||0
8|amount|TEXT|1||0
9|comment|TEXT|0||0

### owner
Joint
Self
Spouse
Child

### ticker
distinct: 1329

### transaction_type
Sale (Partial)
Purchase
Sale (Full)
Exchange

### amount
$1,001 - $15,000
$15,001 - $50,000
$100,001 - $250,000
$50,001 - $100,000
$500,001 - $1,000,000
$250,001 - $500,000
$1,000,001 - $5,000,000
$5,000,001 - $25,000,000
