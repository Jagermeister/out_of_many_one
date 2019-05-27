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