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



### Migrating old methods to controller
def annual_reports_parse_and_store(efd_storage, efd_parse):
    annual_reports = efd_storage.annual_reports_get()
    #annual_reports = [efd_storage.annual_reports_get()[5]]
    for report in annual_reports:
        (report_key, link_key,
        one, two, three, four_a, four_b, five,
        six, seven, eight, nine, ten, comment) = report

        #print(report_key, nine)
        #parse_testing(six)

        charity = efd_parse.annual_report_charity_parse(report_key, one)
        ##efd_storage.annual_report_charity_add(charity)

        earned_income = efd_parse.annual_report_earned_income_parse(report_key, two)
        ##efd_storage.annual_report_earned_income_add(earned_income)

        asset = efd_parse.annual_report_asset_parse(report_key, three)
        ##efd_storage.annual_report_asset_add(asset)

        ptr = efd_parse.annual_report_ptr_parse(report_key, four_a)
        ##efd_storage.annual_report_ptr_add(ptr)

        transaction = efd_parse.annual_report_transaction_parse(report_key, four_b)
        ##efd_storage.annual_report_transaction_add(transaction)

        gift = efd_parse.annual_report_gift_parse(report_key, five)
        ##efd_storage.annual_report_gift_add(gift)

        travel = efd_parse.annual_report_travel_parse(report_key, six)
        ##efd_storage.annual_report_travel_add(travel)

        liability = efd_parse.annual_report_liability_parse(report_key, seven)
        ##efd_storage.annual_report_liability_add(liability)

        position = efd_parse.annual_report_position_parse(report_key, eight)
        ##efd_storage.annual_report_position_add(position)

        agreement = efd_parse.annual_report_agreement_parse(report_key, nine)
        ##efd_storage.annual_report_agreement_add(agreement)