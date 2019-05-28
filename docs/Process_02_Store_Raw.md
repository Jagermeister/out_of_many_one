# Storing Raw Requests and Responses

We want to disconnect document retrieval with data parsing. Document retrieval should only occur when there are new or updated items. If data parsing was coupled with the download process, then we would unnecessarily waste time and resources when we test out new revisions of our parsing framework.

## [SQLite](https://docs.python.org/3/library/sqlite3.html)
This lightweight disk-based database will allow us to start [storing data relationally](https://en.wikipedia.org/wiki/Relational_database). We will be able to reduce data duplication by enforcing a [level of normalization](https://en.wikipedia.org/wiki/Database_normalization). These efforts will allow us to better transform the data when it comes time to report.

```SQL
CREATE TABLE [IF NOT EXISTS] report (
    report_key INTEGER PRIMARY KEY,
    report_hash TEXT,
    name_first TEXT,
    name_last TEXT,
    filer_type TEXT,
    report_type TEXT,
    filed_date TEXT
);
```
What was all the fuss about if we are storing everything as unparsed text? It is true that the raw report table is unstructured - perhaps you would explore a different storage mechanism for this step. Keeping this in SQLite will allow for easy integration, linking the raw report to the parsed data records. We will use the `report_hash` column to allow us to quickly determine if we have already seen a record.

### Table Creation
```python
    connection = sqlite3.connect('./data/efd.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS report (
            report_key INTEGER PRIMARY KEY,
            report_hash TEXT,
            name_first TEXT,
            name_last TEXT,
            filer_type TEXT,
            report_type TEXT,
            filed_date TEXT
        );
    ''')

    connection.commit()
```
### Record Insertion
```python
    test_reports = [
        (
            '372c668ddaf5d9a5fe3e34ad6b0e144488e17f5f2170d6f7e79534d6871d7587',
            'Cory A', 'Booker', 'Senator',
            '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>',
            '05/15/2019'
        ), (
            'b6b1f6ad88f11841d0bfb02ccc09d785fa2cfa6b14706cf5061797714a722e85',
            'Cory A', 'Booker', 'Senator',
            '<a href="/search/view/annual/f0167931-f249-49ac-93f7-bc2013e48a27/" target="_blank">Annual Report for CY 2014</a>',
            '08/13/2015'
        ), (
            'db94317b721ddd6d31c4686e5cbeaad24933dd26cafc128700700fddc20cffc1',
            'Cory A', 'Booker', 'Senator',
            '<a href="/search/view/annual/0ab31d94-7108-4d1a-8d13-098284271d5f/" target="_blank">Annual Report for CY 2016</a>',
            '08/09/2017'
        ), (
            '2b0d281a4317cca0667e25d9214bb58d06b4e8356cf05f4dc5db41ce83d90a03',
            'Cory A', 'Booker', 'Senator',
            '<a href="/search/view/annual/25bc76e7-c7c3-4d04-b215-d752c94dd47a/" target="_blank">Annual Report for CY 2013 (Amendment 1)</a>',
            '08/13/2015'
        )
    ]
    cursor.executemany('''
        INSERT INTO report (
            report_hash,
            name_first,
            name_last,
            filer_type,
            report_type,
            filed_date
        ) VALUES (
            ?, ?, ?, ?, ?, ?
        )
    ''', test_reports)

    connection.commit()
```
### Reading Records
```python
    cursor.execute('''
        SELECT *
        FROM report;
    ''')

    reports = cursor.fetchall()
    connection.close()

    for report in reports:
        print(report)
```
Confirming our test records made it 
```python
('372c668ddaf5d9a5fe3e34ad6b0e144488e17f5f2170d6f7e79534d6871d7587', 'Cory A', 'Booker', 'Senator', '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>', '05/15/2019')

('b6b1f6ad88f11841d0bfb02ccc09d785fa2cfa6b14706cf5061797714a722e85', 'Cory A', 'Booker', 'Senator', '<a href="/search/view/annual/f0167931-f249-49ac-93f7-bc2013e48a27/" target="_blank">Annual Report for CY 2014</a>', '08/13/2015')

('db94317b721ddd6d31c4686e5cbeaad24933dd26cafc128700700fddc20cffc1', 'Cory A', 'Booker', 'Senator', '<a href="/search/view/annual/0ab31d94-7108-4d1a-8d13-098284271d5f/" target="_blank">Annual Report for CY 2016</a>', '08/09/2017')

('2b0d281a4317cca0667e25d9214bb58d06b4e8356cf05f4dc5db41ce83d90a03', 'Cory A', 'Booker', 'Senator', '<a href="/search/view/annual/25bc76e7-c7c3-4d04-b215-d752c94dd47a/" target="_blank">Annual Report for CY 2013 (Amendment 1)</a>', '08/13/2015')
```

### Hash Identity
Later we will want a quick way to determine if we have seen a record without needing to compare every field. We can construct a quick hash based on the column values.
```python
import hashlib

JOIN_KEY = '+|+' # Column separator

record = (
    'Cory A', 'Booker', 'Senator',
    '<a href="/search/view/annual/8796c940-0d0d-4579-83ce-edb3d373780c/" target="_blank">Annual Report for CY 2018</a>',
    '05/15/2019'
)

record_text = JOIN_KEY.join(record).encode('utf-8')
hash_identity = hashlib.sha256(record_text).hexdigest()

print(hash_identity)
```
>372c668ddaf5d9a5fe3e34ad6b0e144488e17f5f2170d6f7e79534d6871d7587

### Up Next: Parsing documents into data




