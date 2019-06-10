""" Parsing Annual Report header """

from src.parse.section_template import SectionTemplate

class HeaderParser(SectionTemplate):
    """ Annual Report for The Honorable """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'.*?(\d{4})?.*?</h1><h2 class="filedReport">'
            r' (.*?) </h2>.*?'
            r'Filed (\d\d/\d\d/\d\d\d\d @ \d?\d:?\d?\d? .M)')

    def handle_match(self, key, match):
        """ Cast calendar year to integer """
        super().handle_match(key, match)
        if match[1]:
            match[1] = int(match[1])
        else:
            match[1] = None
