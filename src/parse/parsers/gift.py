""" Parsing Annual Report Section 5: Gifts """

from src.parse.section_template import SectionTemplate

class GiftParser(SectionTemplate):
    """ Did you, your spouse, or dependent child receive any reportable gift during the reporting period? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td>(\d\d/\d\d/\d{4})</td><td>(.*?)</td><td>(.*?)</td>'
            r'<td>\$(.*?)</td><td>(.*?)<div class="muted">(.*?)</div></td>')

    def handle_match(self, key, match):
        """ Parse USD to float """
        super().handle_match(key, match)
        match[5] = float(match[5].replace(',', ''))
