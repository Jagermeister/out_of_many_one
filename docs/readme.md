# Out of many, one
_e pluribus unum_


Using Python to bring transparency and insights into the financial disclosures of Senators. Offering insights from capturing, transforming, and reporting on available public data.

This will walk you through each step of creating a robust data gathering and analysis application.


## Installation
I am using Python 3.7 and a virtual environment to contain dependencies with the [venv module](https://docs.python.org/3.7/library/venv.html). Required packages are split between production and development conerns (linting, testing, documentation).
```bash
$ python --version
Python 3.7.3

$ python -m venv env
# Create a virtual environment within folder 'env'

$ source env/scripts/activate
# Activate the virtual environment. You will now see
# "(env)" appearing in front of your terminal.

$ pip install -r devrequirements.txt
# Reading devrequirements and requirements.txt to
# gather and install required packages.

# Open your editor now that the virtual environment is
# setup and dependencies are installed. Do all your work!
$ python main.py

$ deactivate
# Exits the virtual environment once you are done.
```

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
### Round 4
  - Robust Fetching (Rate Limiting, Pagination, Data Discovery, Error Handling)


## Data Description
United States Senitors are required to file [Financial Disclosure Reports](https://www.ethics.senate.gov/public/index.cfm/financialdisclosure) detailing assets, liabilities, travel, agreements, and transactions for both themselves and their spouse. Access to this data is governed by the [Ethics in Government Act of 1978](https://legcounsel.house.gov/Comps/Ethics%20In%20Government%20Act%20Of%201978.pdf) stating:

>1. It shall be unlawful for any person to obtain or use a report:
    1. for any unlawful purpose;
    2. for any commercial purpose, other than by news and communications media for dissemination to the general public;
    3. for determining or establishing the credit rating of any individual; or
    4. for use, directly or indirectly, in the solicitation of money for any political, charitable, or other purpose.
>2. The Attorney General may bring a civil action against any person who obtains or uses a report for any purpose prohibited in paragraph (1) of this subsection. The court in which such action is brought may assess against such person a penalty in any amount not to exceed $10,000. Such remedy shall be in addition to any other remedy available under statutory or common law.

Reports from 2012 to present are available for search at the Senate's [Electronic Financial Disclosure](https://efdsearch.senate.gov/search/home/). Document appear in html for those submitted electronically and as images for those submitted on paper.
