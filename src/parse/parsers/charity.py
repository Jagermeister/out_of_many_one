""" Parsing Annual Report Section 1: Charity """

from src.parse.section_template import SectionTemplate

class CharityParser(SectionTemplate):
    """ Did any individual or organization pay you or your spouse
        more than $200 or donate any amount to a charity on your
        behalf, for an article, speech, or appearance? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td> (\d\d/\d\d/\d{4}) </td><td>(.*?)</td><td>\$(.*?)</td>'
            r'<td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>')

    def handle_match(self, key: int, match) -> None:
        """ Parse USD to float """
        super().handle_match(key, match)
        match[4] = float(match[4].replace(',', ''))
