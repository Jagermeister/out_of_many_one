""" Parsing Annual Report Section 10: Compensation """

from src.parse.section_template import SectionTemplate

class CompensationParser(SectionTemplate):
    """ If this is your first report, or you are a candidate
        did you receive compensation of more than $5,000
        from a single source in the two prior years? """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td> (\d+)</td><td>(.*?)<div class="muted">(.*?)</div>'
            r'<td>(.*?)</td></td>')
