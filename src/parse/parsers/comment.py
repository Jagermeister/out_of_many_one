""" Parsing Annual Report: Comments and Attachments """

import re

from src.parse.section_template import SectionTemplate

#ATTACHMENT_NONE = '<em class="muted">No attachments added.</em>'
ATTACHMENT_EXPRESSION = r'<td><a href="(.*?)" target="_blank">(.*?)</a></td><td>(.*?M)</td>'

class CommentParser(SectionTemplate):

    def __init__(self):
        super().__init__()
        self.pattern = r'(<em class="muted">No attachments added.</em>|<tbody>(.*?)</tbody>).*?(<em class="text-muted">No comments added.</em>|<h4 class="h5">Comments</h4> (.*?) </div>)'
        self.attachment_rx = re.compile(ATTACHMENT_EXPRESSION)

    def parse_internal(self, key, match):
        super().parse_internal(key, match)
        attachment_match = match[2]
        if attachment_match:
            matches = self.attachment_rx.findall(attachment_match)
            match[2] = [list(m) for m in matches]
