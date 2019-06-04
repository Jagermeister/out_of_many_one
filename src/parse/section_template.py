""" Abstract class for concrete parsing of report section """

import re

class SectionTemplate:

    def __init__(self):
        self.rx = None
        self.pattern = None

    def setup(self):
        if not self.rx:
            self.rx = re.compile(self.pattern)

    def clean_text(self, text):
        cleaned = text.replace('\n', '')
        cleaned = re.sub(r'\s\s+', ' ', cleaned)
        return cleaned

    def parse(self, key, text_raw):
        self.setup()
        text = self.clean_text(text_raw)
        matches = self.rx.findall(text)
        results = [list(match) for match in matches]
        for match in results:
            self.parse_internal(key, match)

        return results

    def parse_internal(self, key, match):
        match.insert(0, key)