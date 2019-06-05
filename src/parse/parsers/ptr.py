""" Parsing Annual Report Section 4: Periodic Transaction Report """

from src.parse.section_template import SectionTemplate

class PTRParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td>(\d+)</td><td> (\d\d/\d\d/\d{4}) </td><td>(.*?)</td><td> (.*?) </td><td> (.*?) </td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[4] = match[4].strip()
        match[5] = match[5].strip()
