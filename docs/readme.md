# Out of many, one

_e pluribus unum_

Using Python to bring transparency to the financial disclosures of Senators. Offering insights from capturing, transforming, and reporting on available public data.

A detailed walkthrough each step of creating a robust data gathering and analysis application.

## Installation

Python 3.7 and a virtual environment allows us to contain dependencies with the [venv module](https://docs.python.org/3.7/library/venv.html). Required packages are split between production and development conerns (linting, testing, documentation).

```bash
$ python --version
Python 3.7.3

$ python -m venv env
# Create a virtual environment within ./env/

$ source env/scripts/activate   #Windows
$ source env/bin/activate       #Linux
# Activate the virtual environment. You will now see
# "(env)" appearing in front of your terminal.

$ pip install -r devrequirements.txt
# Installing packages from devrequirements.txt.

$ mkdir data
# Create the folder for the SQLite db file - This is by default you can change the location in the Storage module

# Now your editor will recognize the virtual environment.
$ python main.py

# Running tests
$ python -m pytest

$ deactivate
# Exits the virtual environment once you are done.
```

## Data Description

United States Senitors are required to file [Financial Disclosure Reports](https://www.ethics.senate.gov/public/index.cfm/financialdisclosure) detailing assets, liabilities, travel, agreements, and transactions for both themselves and their spouse. Access to this data is governed by the [Ethics in Government Act of 1978](https://legcounsel.house.gov/Comps/Ethics%20In%20Government%20Act%20Of%201978.pdf) stating:

> 1.  It shall be unlawful for any person to obtain or use a report:
>    - for any unlawful purpose;
>    - for any commercial purpose, other than by news and communications media for dissemination to the general public;
>    - for determining or establishing the credit rating of any individual; or
>    - for use, directly or indirectly, in the solicitation of money for any political, charitable, or other purpose.
> 2.  The Attorney General may bring a civil action against any person who obtains or uses a report for any purpose prohibited in paragraph (1) of this subsection. The court in which such action is brought may assess against such person a penalty in any amount not to exceed \$10,000. Such remedy shall be in addition to any other remedy available under statutory or common law.

Reports from 2012 to present are available for search at the Senate's [Electronic Financial Disclosure](https://efdsearch.senate.gov/search/home/). Document appear in html for those submitted electronically and as images for those submitted on paper.

## Process

### Round 1

- [Fetch Electronic Filing Links](./Process_01_Fetch.md)
- [Store Document Links](./Process_02_Store_Document_Links.md)
- [Parse Document Links into Data](./Process_03_Parse.md)
- [Relational Storage](./Process_04_Relational_Storage.md)
- Data Integration

### Round 2

- Fetch Electronic Filing Document
- Store
- Parse
- Storage

### Round 3

- Data Transformation
- Visualization
