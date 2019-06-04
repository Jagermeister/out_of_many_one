""" Parsing Annual Report Section 1: Charity """

from src.parse.section_template import SectionTemplate

class CharityParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td> (\d\d/\d\d/\d{4}) </td><td>(.*?)</td><td>\$(.*?)</td><td> (.*?) <div class="muted">(.*?)</div></td><td>(.*?)</td>'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[4] = float(match[4].replace(',', ''))
