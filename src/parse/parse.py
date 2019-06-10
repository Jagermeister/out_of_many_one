""" Break raw data into attributes """

import re

from src.parse.parsers.header import HeaderParser
from src.parse.parsers.charity import CharityParser
from src.parse.parsers.income import IncomeParser
from src.parse.parsers.asset import AssetParser
from src.parse.parsers.ptr import PTRParser
from src.parse.parsers.transaction import TransactionParser
from src.parse.parsers.gift import GiftParser
from src.parse.parsers.travel import TravelParser
from src.parse.parsers.liability import LiabilityParser
from src.parse.parsers.position import PositionParser
from src.parse.parsers.agreement import AgreementParser
from src.parse.parsers.compensation import CompensationParser
from src.parse.parsers.comment import CommentParser


RAW_DOCUMENT_EXPRESSION = r'view/(.*?)/(?:regular/)?(.*?)/".*?>(.*?)</a>'

class Parse: # pylint: disable=too-many-instance-attributes
    """ Given text, produce attributes """

    def __init__(self):
        self.re_document_link = None
        self.header_parser = HeaderParser()
        self.charity_parser = CharityParser()
        self.income_parser = IncomeParser()
        self.asset_parser = AssetParser()
        self.ptr_parser = PTRParser()
        self.transaction_parser = TransactionParser()
        self.gift_parser = GiftParser()
        self.travel_parser = TravelParser()
        self.liability_parser = LiabilityParser()
        self.position_parser = PositionParser()
        self.agreement_parser = AgreementParser()
        self.compensation_parser = CompensationParser()
        self.comment_parser = CommentParser()

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

    def parse_transaction(self, key, text):
        return self.transaction_parser.parse(key, text)

    def parse_gift(self, key, text):
        return self.gift_parser.parse(key, text)

    def parse_travel(self, key, text):
        return self.travel_parser.parse(key, text)

    def parse_liability(self, key, text):
        return self.liability_parser.parse(key, text)

    def parse_position(self, key, text):
        return self.position_parser.parse(key, text)

    def parse_agreement(self, key, text):
        return self.agreement_parser.parse(key, text)

    def parse_compensation(self, key, text):
        return self.compensation_parser.parse(key, text)

    def parse_comment(self, key, text):
        return self.comment_parser.parse(key, text)

    def __document_link_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_document_link:
            self.re_document_link = re.compile(RAW_DOCUMENT_EXPRESSION)
        return self.re_document_link

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
