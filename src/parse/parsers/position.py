""" Parsing Annual Report Section 8: Positions """

from src.parse.section_template import SectionTemplate

class PositionParser(SectionTemplate):
    """ Did you hold any outside positions during the reporting period? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td>(.*?)</td><td> (.*?) </td>'
            r'<td> (.*?) <div class="muted"> (.*?) </div></td>'
            r'<td> (.*?) </td><td>(.*?)</td>')
