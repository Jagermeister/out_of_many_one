""" Encapsulate Dollar Value to storage keys """

from src.store.sql import (
    DOLLAR_VALUE_TABLE_CREATE,
    DOLLAR_VALUE_DEFAULTS,
    DOLLAR_VALUE_POPULATE,
    DOLLAR_VALUES_READ
)
from src.store.entities.utility import fetch_table_values


__DOLLAR_VALUES = {}
__UNKNOWN_KEY = None

__REMAP_MILLION = 'Over $1,000,000 and held independently by spouse or dependent child'

def __fetch_dollar_values():
    if not __DOLLAR_VALUES:
        global __UNKNOWN_KEY # pylint: disable=global-statement
        dollar_values = fetch_table_values(
            DOLLAR_VALUE_TABLE_CREATE,
            DOLLAR_VALUE_DEFAULTS,
            DOLLAR_VALUE_POPULATE,
            DOLLAR_VALUES_READ
        )
        for value in dollar_values:
            key, name, _, _ = value
            __DOLLAR_VALUES[name] = key
            if name == 'UNKNOWN':
                __UNKNOWN_KEY = key
            elif name == '$1,000,001 - $5,000,000':
                __DOLLAR_VALUES[__REMAP_MILLION] = key

def dollar_value_to_key(dollar_value):
    """ Convert dollar value ranges to storage keys
    Args:
        dollar_value: str - "$15,001 - $50,000" There are
        predetermined ranges identified for use.
    """
    __fetch_dollar_values()
    if dollar_value in __DOLLAR_VALUES:
        return __DOLLAR_VALUES[dollar_value]

    return __UNKNOWN_KEY
