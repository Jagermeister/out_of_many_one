# Parse Raw Documents
Luckily the Search grid has only a few standard columns returned for us to look at.

```Python
# First Name (Middle), Last Name (Suffix), Filer Type, Report Type, Date
'Cory A', 'Booker', 'Senator', '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>', '05/15/2019'
```

The only column needing extra attention is the Report Type. We can break this down into the following data elements:

`<a href="/search/view/{DOCUMENT_TYPE}/{DOCUMENT_ID}/" target="_blank">{DOCUMENT_NAME}</a>`

```python
import re

DOCUMENT_EXPRESSION = r'view/(.*?)/(.*?)/".*?>(.*?)</a>'

test_link = '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>'

match = re.search(DOCUMENT_EXPRESSION, test_link)
print(match.groups())
```
>('annual', '8796c940-0d0d-4579-83ce-edb3d373780c', 'Annual Report for CY 2018')

This is straight forward now as we work on the process flow. Later we will tackle the more complicated parsing required for the electronic financial disclosures.

## Data Normalization
We won't just be adding these new document fields to the existing attributes and inserting them into the same table. Here we will work to reduce data duplication by reusing already known entities. For instance, we should have a reference to each Senator's name and not need to keep storing the actual text values for first and last name.

### Filer
Who is the person that the document is filed for?
```SQL
CREATE TABLE IF NOT EXISTS filer (
    filer_key INTEGER PRIMARY KEY,
    name_first TEXT NOT NULL,
    name_last TEXT NOT NULL
)
```
|First|Last|
|-----|----|
|Cory A|Booker|

### Filer Type
What is the role of the person who is filing?
```SQL
CREATE TABLE IF NOT EXISTS filer_type (
    filer_type_key INTEGER PRIMARY KEY,
    filer_name TEXT NOT NULL,
    is_senator INTEGER NOT NULL,
    is_candidate INTEGER NOT NULL,
    is_former_senator INTEGER NOT NULL
)
```
|Name|Senator?|Candidate?|Former Senator?|
|----|--------|----------|---------------|
|Senator|Yes|No|No|
|Candidate|No|Yes|No|
|Former Senator|No|No|Yes|

### Document Type
How was the document filed?
```SQL
CREATE TABLE IF NOT EXISTS document_type (
    document_type_key INTEGER PRIMARY KEY,
    document_type_name TEXT NOT NULL,
    is_electronic INTEGER NOT NULL,
    is_paper INTEGER NOT NULL
)
```
|Name|Electronic?|Paper?|
|----|-----------|------|
|Electronic|Yes|No|
|Paper|No|Yes|

### Document
Connecting all the attributes to the report.
```SQL
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
)
```
|Filer|Filer Type|Document Type|ID|Name|Year|Date|
|-----|----------|-------------|--|----|----|----|
|1|1|1|8796c940-0d0d-4579-83ce-edb3d373780c|Annual Report for CY 2018|2018|05/15/2019|