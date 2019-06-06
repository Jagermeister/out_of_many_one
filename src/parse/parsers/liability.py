""" Parsing Annual Report Section 7: Liability """

from src.parse.section_template import SectionTemplate

class LiabilityParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td> (\d+)</td><td> (\d+) </td><td>(.*?)</td><td>(.*?)</td><td> (.*?)</td><td> (.*?)</td><td>(.*?)</td><td> (.*?) <div class="muted">(.*?)</div></td><td>(.*?)</td>'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[2] = int(match[2])
