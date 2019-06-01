""" Break raw data into attributes """

import re

RAW_DOCUMENT_EXPRESSION = r'view/(.*?)/(regular/)?(.*?)/".*?>(.*?)</a>'
ANNUAL_REPORT_CHARITY_EXPRESSION = r'<td>(\d+)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>\$(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>'
ANNUAL_REPORT_EARNED_INCOME_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)<br/><div class="muted">(.*?)</div></td><td>\$(.*?)</td>'
ANNUAL_REPORT_ASSET_EXPRESSION = r'<td>(.*?)</td><td class="span4">(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_PTR_EXPRESSION = r'<td>(\d+)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_TRANSACTION_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_TRAVEL_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>'
ANNUAL_REPORT_POSITION_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td>'
ANNUAL_REPORT_AGREEMENT_EXPRESSION = r'<td>(\d+)</td><td>(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td>'

class Parse:
    """ Given text, produce attributes """

    def __init__(self):
        self.re_document_link = None
        self.re_annual_report_charity = None
        self.re_annual_report_income = None
        self.re_annual_report_asset = None
        self.re_annual_report_ptr = None
        self.re_annual_report_transaction = None
        self.re_annual_report_travel = None
        self.re_annual_report_position = None
        self.re_annual_report_agreement = None

    def __document_link_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_document_link:
            self.re_document_link = re.compile(RAW_DOCUMENT_EXPRESSION)
        return self.re_document_link

    def __annual_report_charity_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_charity:
            self.re_annual_report_charity = re.compile(ANNUAL_REPORT_CHARITY_EXPRESSION)
        return self.re_annual_report_charity

    def __annual_report_earned_income_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_income:
            self.re_annual_report_income = re.compile(ANNUAL_REPORT_EARNED_INCOME_EXPRESSION)
        return self.re_annual_report_income

    def __annual_report_asset_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_asset:
            self.re_annual_report_asset = re.compile(ANNUAL_REPORT_ASSET_EXPRESSION)
        return self.re_annual_report_asset

    def __annual_report_ptr_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_ptr:
            self.re_annual_report_ptr = re.compile(ANNUAL_REPORT_PTR_EXPRESSION)
        return self.re_annual_report_ptr

    def __annual_report_transaction_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_transaction:
            self.re_annual_report_transaction = re.compile(ANNUAL_REPORT_TRANSACTION_EXPRESSION)
        return self.re_annual_report_transaction

    def __annual_report_travel_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_annual_report_travel:
            self.re_annual_report_travel = re.compile(ANNUAL_REPORT_TRAVEL_EXPRESSION)
        return self.re_annual_report_travel

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

    def annual_report_charity_parse(self, report_key, charity):
        """ Convert into structured data """
        text = self.__replace_tab_new_line(charity)
        pattern = self.__annual_report_charity_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[3] = float(result[3].replace(',', ''))
            result.insert(0, report_key)
        return results

    def annual_report_earned_income_parse(self, report_key, earned_income):
        """ Convert into structured data """
        text = self.__replace_tab_new_line(earned_income)
        pattern = self.__annual_report_earned_income_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[5] = float(result[5].replace(',', ''))
            result.insert(0, report_key)
        return results

    def annual_report_asset_parse(self, report_key, asset):
        """ Convert into structured data """
        text = self.__replace_tab_new_line(asset)
        pattern = self.__annual_report_asset_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[0] = float(result[0])
            result.insert(0, report_key)
        return results

    def annual_report_ptr_parse(self, report_key, ptr):
        text = self.__replace_tab_new_line(ptr)
        pattern = self.__annual_report_ptr_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[3] = result[3].strip()
            result[4] = result[4].strip()
            result.insert(0, report_key)
        return results

    def annual_report_transaction_parse(self, report_key, transaction):
        text = self.__replace_tab_new_line(transaction)
        pattern = self.__annual_report_transaction_regex()
        matches = pattern.findall(text)
        results = [list(match) for match in matches]
        for result in results:
            result[3] = result[3].strip()
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
