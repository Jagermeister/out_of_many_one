""" Parsing Annual Report Section 8: Positions """

from src.parse.section_template import SectionTemplate

class PositionParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td>(.*?)</td><td> (.*?) </td><td> (.*?) <div class="muted"> (.*?) </div></td><td> (.*?) </td><td>(.*?)</td>'

