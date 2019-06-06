""" Parsing Annual Report header """

from src.parse.section_template import SectionTemplate

class HeaderParser(SectionTemplate):
    """ Annual Report for The Honorable """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'Annual Report for Calendar (\d{4}) </h1><h2 class="filedReport">'
            r' The Honorable (.*?) </h2><p class="muted font-weight-bold">'
            r'<i class="fa fa-folder-open"></i> Filed (\d\d/\d\d/\d\d\d\d @ \d\d:\d\d .M)')

    def handle_match(self, key, match):
        """ Cast calendar year to integer """
        super().handle_match(key, match)
        match[1] = int(match[1])
