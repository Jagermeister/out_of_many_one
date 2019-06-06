""" Parsing Annual Report Section 6: Travel """

from src.parse.section_template import SectionTemplate

class TravelParser(SectionTemplate):
    """ Did you, your spouse, or dependent child receive any reportable travel? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td>(.*?)</td><td>(.*?)</td>'
            r'<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
            r'<td>(.*?)<div class="muted">(.*?)</div></td><td>(.*?)</td>')
