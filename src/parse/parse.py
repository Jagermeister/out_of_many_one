""" Break raw data into attributes """

import re

RAW_DOCUMENT_EXPRESSION = r'view/(.*?)/(?:regular/)?(.*?)/".*?>(.*?)</a>'
ANNUAL_REPORT_TRANSACTION_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_TRAVEL_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>'
ANNUAL_REPORT_POSITION_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_AGREEMENT_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_GIFT_EXPRESSION = r'<td>(\d+)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td><td>\$(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td>'
ANNUAL_REPORT_LIABILITY_EXPRESSION = r'<td>(\d+)</td><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>'

from src.parse.parsers.header import HeaderParser
from src.parse.parsers.charity import CharityParser
from src.parse.parsers.income import IncomeParser
from src.parse.parsers.asset import AssetParser
from src.parse.parsers.ptr import PTRParser

class Parse:
    """ Given text, produce attributes """

    def __init__(self):
        self.re_document_link = None
        self.re_annual_report_transaction = None
        self.re_annual_report_gift = None
        self.re_annual_report_travel = None
        self.re_annual_report_liability = None
        self.re_annual_report_position = None
        self.re_annual_report_agreement = None
        self.header_parser = HeaderParser()
        self.charity_parser = CharityParser()
        self.income_parser = IncomeParser()
        self.asset_parser = AssetParser()
        self.ptr_parser = PTRParser()

    def parse_header(self, key, text):
        return self.header_parser.parse(key, text)

    def parse_charity(self, key, text):
        return self.charity_parser.parse(key, text)

    def parse_income(self, key, text):
        return self.income_parser.parse(key, text)

    def parse_asset(self, key, text):
        return self.asset_parser.parse(key, text)

    def parse_ptr(self, key, text):
        return self.ptr_parser.parse(key, text)

    def __document_link_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_document_link:
            self.re_document_link = re.compile(RAW_DOCUMENT_EXPRESSION)
        return self.re_document_link

    def __annual_report_transaction_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_transaction:
            self.re_annual_report_transaction = re.compile(ANNUAL_REPORT_TRANSACTION_EXPRESSION)
        return self.re_annual_report_transaction

    def __annual_report_gift_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_gift:
            self.re_annual_report_gift = re.compile(ANNUAL_REPORT_GIFT_EXPRESSION)
        return self.re_annual_report_gift

    def __annual_report_travel_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_travel:
            self.re_annual_report_travel = re.compile(ANNUAL_REPORT_TRAVEL_EXPRESSION)
        return self.re_annual_report_travel

    def __annual_report_liability_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_liability:
            self.re_annual_report_liability = re.compile(ANNUAL_REPORT_LIABILITY_EXPRESSION)
        return self.re_annual_report_liability

    def __annual_report_position_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_position:
            self.re_annual_report_position = re.compile(ANNUAL_REPORT_POSITION_EXPRESSION)
        return self.re_annual_report_position

    def __annual_report_agreement_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_agreement:
            self.re_annual_report_agreement = re.compile(ANNUAL_REPORT_AGREEMENT_EXPRESSION)
        return self.re_annual_report_agreement

    def document_link_parse(self, document_link):
        """ Break document link into the underlying data
        Args:
            document_link: str - A web link with a title
        Returns:
            (document_type, document_id, document_name)
        """
        pattern = self.__document_link_regex()
        match = pattern.search(document_link)
        return match.groups()

    def document_type_standardize(self, document_type_name):
        """ Convert document type to proper document type name"""
        if document_type_name == "ptr":
            return "Periodic Transaction Report"

        if document_type_name == "extension-notice":
            return "Due Date Extension"
        
        if document_type_name == "paper":
            return "UNKNOWN"

        return document_type_name

    def __replace_tab_new_line(self, text):
        """ Remove unused formatting for matching """
        treated = text.replace('\t', '')
        return treated.replace('\n', '')

    def annual_report_transaction_parse(self, report_key, transaction):
        text = self.__replace_tab_new_line(transaction)
        pattern = self.__annual_report_transaction_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[3] = result[3].strip()
            result.insert(0, report_key)
        return results

    def annual_report_gift_parse(self, report_key, gift):
        text = self.__replace_tab_new_line(gift)
        pattern = self.__annual_report_gift_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[5] = float(result[4].replace(',', ''))
            result.insert(0, report_key)
        return results

    def annual_report_travel_parse(self, report_key, travel):
        text = self.__replace_tab_new_line(travel)
        pattern = self.__annual_report_travel_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result.insert(0, report_key)
        return results

    def annual_report_liability_parse(self, report_key, liability):
        text = self.__replace_tab_new_line(liability)
        pattern = self.__annual_report_liability_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[1] = int(result[1])
            result.insert(0, report_key)
        return results

    def annual_report_position_parse(self, report_key, position):
        text = self.__replace_tab_new_line(position)
        pattern = self.__annual_report_position_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result.insert(0, report_key)
        return results

    def annual_report_agreement_parse(self, report_key, agreement):
        text = self.__replace_tab_new_line(agreement)
        pattern = self.__annual_report_agreement_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result.insert(0, report_key)
        return results
