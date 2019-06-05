""" Parsing Annual Report Section 2: Income """

from src.parse.section_template import SectionTemplate

class IncomeParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td> (.*?) </td><td> (.*?) </td><td> (.*?)<br/><div class="muted">(.*?)</div></td><td>.*?\$(.*?)</td>'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[6] = float(match[6].replace(',', ''))
