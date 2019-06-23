""" Parsing Annual Report: Comments and Attachments """

import re

from src.parse.section_template import SectionTemplate

ATTACHMENT_EXPRESSION = r'<td><a href="(.*?)" target="_blank">(.*?)</a></td><td>(.*?M)</td>'

class CommentParser(SectionTemplate):
    """ Attachments & Comments """

    def __init__(self):
        super().__init__()
        self.pattern = (
            r'(<em class="muted">No attachments added.</em>|<tbody>(.*?)</tbody>).*?'
            r'(<em class="text-muted">No comments added.</em>|'
            r'<h4 class="h5">Comments</h4>(.*?)</div>)')
        self.attachment_rx = re.compile(ATTACHMENT_EXPRESSION)

    def handle_match(self, key: int, match) -> None:
        """ Parse attachment section when available """
        super().handle_match(key, match)
        attachment_match = match[2]
        if attachment_match:
            matches = self.attachment_rx.findall(attachment_match)
            match[2] = [list(m) for m in matches]
