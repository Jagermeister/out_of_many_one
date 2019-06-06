""" Parsing Annual Report Section 10: Compensation """

from src.parse.section_template import SectionTemplate

class CompensationParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td> (.*?) <div class="muted">(.*?)</div><td>(.*?)</td></td>'
