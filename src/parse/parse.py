""" Break raw data into attributes """

import re

RAW_DOCUMENT_EXPRESSION = r'view/(.*?)/(regular/)?(.*?)/".*?>(.*?)</a>'

class Parse:
    """ Given text, produce attributes """

    def __init__(self):
        self.re_document_link = None

    def __document_link_regex(self):
        """ Produce a compiled regular expression """
        if not self.re_document_link:
            self.re_document_link = re.compile(RAW_DOCUMENT_EXPRESSION)
        return self.re_document_link

    def document_link_parse(self, document_link):
        """ Break document link into the underlying data
        Args:
            document_link: str - A web link with a title
        Returns:
            (document_type, document_id, document_name)
        """
        pattern = self.__document_link_regex()
        match = pattern.search(document_link)
        return match.groups()

    def document_type_standardize(self, document_type_name):
        """ Convert document type to proper document type name"""
        if document_type_name == "ptr":
            return "Periodic Transaction Report"

        if document_type_name == "extension-notice":
            return "Due Date Extension"
        
        if document_type_name == "paper":
            return "UNKNOWN"

        return document_type_name
