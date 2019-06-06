""" Parsing Annual Report Section 4b: Transactions """

from src.parse.section_template import SectionTemplate

class TransactionParser(SectionTemplate):
    """ Did you, your spouse, or dependent child buy, sell,
        or exchange an asset that exceeded $1,000? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
            r'<td>(.*?)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td>')
