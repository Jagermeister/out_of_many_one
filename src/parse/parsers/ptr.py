""" Parsing Annual Report Section 4a: Periodic Transaction Report """

from src.parse.section_template import SectionTemplate

class PTRParser(SectionTemplate):
    """ In this section, electronically filed periodic transaction
        report (PTR) transactions are displayed for you. """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td>(\d+)</td><td> (\d\d/\d\d/\d{4}) </td><td>(.*?)</td><td> (.*?) </td>'
            r'<td> (.*?) </td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>')
