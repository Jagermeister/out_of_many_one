""" Parsing Annual Report Section 3: Assets """

from src.parse.section_template import SectionTemplate

class AssetParser(SectionTemplate):
    """ Did you, your spouse, or dependent child own any asset worth more than $1000,
        have a deposit account with a balance over $5,000,
        or receive income of more than $200 from an asset?
    """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'<td>(.*?)</td><td class="span4">(.*?)</td><td>(.*?)</td>'
            r'<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>')

    def handle_match(self, key, match):
        """ Parse USD to float """
        super().handle_match(key, match)
        match[1] = float(match[1].replace(',', ''))
