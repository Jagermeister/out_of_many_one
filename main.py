""" Entry point for _Out of many, one_ attempt to capture, transform,
    and report on United States Senators' Financial Disclosures.  """

from src.scrape.efd import EFD

APP = EFD()
APP.login()
reports_response = APP.search('booker')
for key in reports_response:
    print(key, reports_response[key])
