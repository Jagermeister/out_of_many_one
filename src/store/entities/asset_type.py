""" Encapsulate Asset Type to storage keys """

from src.store.sql import (
    ASSET_TYPE_TABLE_CREATE,
    ASSET_TYPE_DEFAULTS,
    ASSET_TYPE_POPULATE,
    ASSET_TYPES_READ
)
from src.store.entities.utility import fetch_table_values


__ASSET_TYPES = {}
__UNKNOWN_KEY = None

def __fetch_asset_types():
    if not __ASSET_TYPES:
        global __UNKNOWN_KEY # pylint: disable=global-statement
        asset_types = fetch_table_values(
            ASSET_TYPE_TABLE_CREATE,
            ASSET_TYPE_DEFAULTS,
            ASSET_TYPE_POPULATE,
            ASSET_TYPES_READ
        )
        for value in asset_types:
            key, name = value
            __ASSET_TYPES[name] = key
            if name == 'UNKNOWN':
                __UNKNOWN_KEY = key

def asset_type_to_key(asset_type: str) -> int:
    """ Convert asset types to storage keys
    Args:
        asset_type: str - "Bank Deposits", "Retirement Plans"
            Describes type of an asset
    """
    __fetch_asset_types()
    if asset_type in __ASSET_TYPES:
        return __ASSET_TYPES[asset_type]

    return __UNKNOWN_KEY
