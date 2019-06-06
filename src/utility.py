""" General purpose functions """

import hashlib
import re

LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'

def hash_from_strings(items):
    """ Produce a hash value from the combination of all str elements """
    item_text = '+|+'.join(items).encode('utf-8')
    return hashlib.sha256(item_text).hexdigest()

def whitespace_condense(text):
    """ Remove duplicate whitespace characters """
    return re.sub(r'\s\s+', ' ', text.replace('\n', ''))
