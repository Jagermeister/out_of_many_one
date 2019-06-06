""" Parsing Annual Report Section 5: Gifts """

from src.parse.section_template import SectionTemplate

class GiftParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td><td>\$(.*?)</td><td> (.*?) <div class="muted">(.*?)</div></td>'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[5] = float(match[5].replace(',', ''))
