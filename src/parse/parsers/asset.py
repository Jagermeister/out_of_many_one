""" Parsing Annual Report Section 3: Assets """

import re

from src.parse.section_template import SectionTemplate

ASSET_SUBTYPE_EXPRESSION = r'([a-zA-Z ]+)(<div class=\"muted\">(.*?)</div>)?$'
ASSET_TYPE_INDEX = 3

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
        self.asset_subtype_rx = re.compile(ASSET_SUBTYPE_EXPRESSION)

    def handle_match(self, key: int, match) -> None:
        """ Parse asset subtype when available """
        super().handle_match(key, match)
        asset_type = match[ASSET_TYPE_INDEX]
        if asset_type:
            matches = self.asset_subtype_rx.findall(asset_type)
            if matches and len(matches[0]) == 3:
                asset_type, _, asset_subtype = matches[0]
                match[ASSET_TYPE_INDEX] = asset_type
                match.insert(ASSET_TYPE_INDEX + 1, asset_subtype)
