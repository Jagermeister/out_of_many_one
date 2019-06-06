""" Parsing Annual Report Section 7: Liability """

from src.parse.section_template import SectionTemplate

class LiabilityParser(SectionTemplate):
    """ Did you, your spouse, or dependent child have a
        liability worth more than $10,000 at any time? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td> (\d+) </td><td>(.*?)</td><td>(.*?)</td>'
            r'<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
            r'<td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>')

    def handle_match(self, key, match):
        """ Parse year to integer """
        super().handle_match(key, match)
        match[2] = int(match[2])
