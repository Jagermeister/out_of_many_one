""" Parsing Annual Report Section 2: Income """

from src.parse.section_template import SectionTemplate

class IncomeParser(SectionTemplate):
    """ Did you or your spouse have reportable earned income or non-investment income? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td> (.*?) </td><td> (.*?) </td>'
            r'<td> (.*?)<br/><div class="muted">(.*?)</div></td><td>.*?\$(.*?)</td>')

    def handle_match(self, key, match):
        """ Parse USD to float """
        super().handle_match(key, match)
        match[6] = float(match[6].replace(',', ''))
