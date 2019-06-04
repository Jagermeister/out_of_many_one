""" Parsing Annual Report header """

from src.parse.section_template import SectionTemplate

class HeaderParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'Annual Report for Calendar (\d{4}) </h1><h2 class="filedReport"> The Honorable (.*?) </h2><p class="muted font-weight-bold"><i class="fa fa-folder-open"></i> Filed (\d\d/\d\d/\d\d\d\d @ \d\d:\d\d .M)'

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        match[1] = int(match[1])
