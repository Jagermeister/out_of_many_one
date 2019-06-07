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

        rows = re.findall('<tr', text)
        if str(self.__class__) == "<class 'src.parse.parsers.header.HeaderParser'>":
            assert len(results) == 1
        elif str(self.__class__) == "<class 'src.parse.parsers.comment.CommentParser'>":
            assert len(results) == 1
            match = results[0]
            assert match[1] == '<em class="muted">No attachments added.</em>' or match[2]
            assert not match[2] or len(rows) - 1 == len(match[2])
            assert match[3] == '<em class="text-muted">No comments added.</em>' or match[4]
        else:
            assert not rows or len(rows) - 1 == len(results)

        return results

    def handle_match(self, key, match): # pylint: disable=no-self-use
        """ Should be overridden to provide concrete handling
            of match results. This may include type casting,
            formatting, or further parsing. At the very least,
            the parent record key is added, preparing for storage.
        """
        for i, _ in enumerate(match):
            match[i] = match[i].strip()

        match.insert(0, key)
