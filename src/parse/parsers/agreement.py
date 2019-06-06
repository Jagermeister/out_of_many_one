""" Parsing Annual Report Section 9: Agreements """

from src.parse.section_template import SectionTemplate

class AgreementParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td> (.*?) </td><td> (.*?) <div class="muted">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td>'
