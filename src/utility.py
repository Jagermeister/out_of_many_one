""" General purpose functions """

import hashlib

def hash_from_strings(items):
    """ Produce a hash value from the combination of all str elements """
    JOIN_KEY = '+|+'
    item_text = JOIN_KEY.join(items).encode('utf-8')
    return hashlib.sha256(item_text).hexdigest()
