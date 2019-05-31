# Parse Document Links

```Python
# First Name (Middle), Last Name (Suffix), Filer Type, Report Type, Date
'Cory A', 'Booker', 'Senator', '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>', '05/15/2019'
```

The only column needing extra attention is the Report Type. We can break this down into the following data elements using [regular expressions](https://docs.python.org/3/library/re.html):

`<a href="/search/view/{DOCUMENT_TYPE}/{DOCUMENT_ID}/" target="_blank">{DOCUMENT_NAME}</a>`

```python
import re

DOCUMENT_EXPRESSION = r'view/(.*?)/(.*?)/".*?>(.*?)</a>'

test_link = '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>'

match = re.search(DOCUMENT_EXPRESSION, test_link)
print(match.groups())
```
>('annual', '8796c940-0d0d-4579-83ce-edb3d373780c', 'Annual Report for CY 2018')

This is straightforward now as we work on the process of fetching, storing, and parsing. Later we will tackle the more complicated parsing required for the electronic financial disclosures.

You could decide to append these three new values to the existing `report` table. When we move on to parsing the financial disclosures you could also have those fields appended. Here I've decided to use a relational database to enforce data quality and improve reporting speed.
- Data Quality: We can ensure only the expected filer type or document types are used by enforcing a hard link between the document and a set of filers. We will be able to quickly review and lookup all filer names without having to scan every document we have ingested.
- Improved Reporting: By using these [data links](https://en.wikipedia.org/wiki/Foreign_key) we will be able to avoid costly text scans. Instead we can use data fields to ask questions like _show me all `is_senator` filers where `filing_date BETWEEN 2014 AND 2016` that held `asset_name = 'Netflix, Inc.' AND asset_amount > 15000`_.

Final implementation is available at [src/parse/parse.py](../src/parse/parse.py).

## Up Next: [Relational Storage](./Process_04_Relational_Storage.md)
