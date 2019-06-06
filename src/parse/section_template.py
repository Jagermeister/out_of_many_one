""" Abstract class for concrete parsing of report section """

import re

from src.utility import whitespace_condense

class SectionTemplate:
    """ Abstract parsing template for report section """

    def __init__(self):
        self.rx = None
        self.pattern = None

    def setup(self):
        """ Compile provided regular expression """
        if not self.rx:
            self.rx = re.compile(self.pattern)

    def parse(self, key, text_raw):
        """ Find all matches based on provided pattern. Allow
            custom logic to be handled in handle_match.
        """
        self.setup()
        text = whitespace_condense(text_raw)
        matches = self.rx.findall(text)
        results = [list(match) for match in matches]
        for match in results:
            self.handle_match(key, match)

        return results

    def handle_match(self, key, match): # pylint: disable=no-self-use
        """ Should be overridden to provide concrete handling
            of match results. This may include type casting,
            formatting, or further parsing. At the very least,
            the parent record key is added, preparing for storage.
        """
        match.insert(0, key)
