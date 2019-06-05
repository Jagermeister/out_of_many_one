""" Parsing Annual Report Section 3: Assets """

from src.parse.section_template import SectionTemplate

class AssetParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'<td>(.*?)</td><td class="span4">(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[1] = float(match[1].replace(',', ''))
