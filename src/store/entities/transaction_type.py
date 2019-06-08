""" Encapsulate Transaction Type to storage keys """

from src.store.sql import (
    TRANSACTION_TYPE_TABLE_CREATE,
    TRANSACTION_TYPE_DEFAULTS,
    TRANSACTION_TYPE_POPULATE,
    TRANSACTION_TYPES_READ
)
from src.store.entities.utility import fetch_table_values


__TRANSACTION_TYPES = {}
__UNKNOWN_KEY = None
__SALE_KEY = None

__SALE_PARTIAL = 'Sale (Full)'
__SALE_FULL = 'Sale (Partial)'

__SALE_TYPES = [
    __SALE_FULL,
    __SALE_PARTIAL,
]


def __fetch_transaction_types():
    if not __TRANSACTION_TYPES:
        global __UNKNOWN_KEY, __SALE_KEY # pylint: disable=global-statement
        transaction_types = fetch_table_values(
            TRANSACTION_TYPE_TABLE_CREATE,
            TRANSACTION_TYPE_DEFAULTS,
            TRANSACTION_TYPE_POPULATE,
            TRANSACTION_TYPES_READ
        )
        for value in transaction_types:
            key, name, _, _, _ = value
            __TRANSACTION_TYPES[name] = key
            if name == 'UNKNOWN':
                __UNKNOWN_KEY = key
            elif name == 'Sale':
                __SALE_KEY = key

def transaction_type_to_key(transaction_type):
    """ Convert dollar value ranges to storage keys
    Args:
        transaction_type: str - "Sale" Describes the
            direction of a transaction (Purchase, Exchange)
    """
    __fetch_transaction_types()
    if transaction_type in __TRANSACTION_TYPES:
        return __TRANSACTION_TYPES[transaction_type]

    if transaction_type in __SALE_TYPES:
        return __SALE_KEY

    return __UNKNOWN_KEY
