""" Entry point for _Out of many, one_ attempt to capture, transform,
    and report on United States Senators' Financial Disclosures.  """

import logging

from src.controller import Controller
from src.utility import LOGGING_FORMAT

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


out_of_many = Controller()
out_of_many.fetch_new_document_links()
out_of_many.parse_document_links()
out_of_many.fetch_new_annual_reports()
out_of_many.parse_annual_reports()
