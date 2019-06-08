""" Encapsulate Asset Owner to storage keys """

from src.store.sql import (
    ASSET_OWNER_TABLE_CREATE,
    ASSET_OWNER_DEFAULTS,
    ASSET_OWNER_POPULATE,
    ASSET_OWNERS_READ
)
from src.store.entities.utility import fetch_table_values


__ASSET_OWNERS = {}
__UNKNOWN_KEY = None

def __fetch_asset_owners():
    if not __ASSET_OWNERS:
        global __UNKNOWN_KEY # pylint: disable=global-statement
        asset_owners = fetch_table_values(
            ASSET_OWNER_TABLE_CREATE,
            ASSET_OWNER_DEFAULTS,
            ASSET_OWNER_POPULATE,
            ASSET_OWNERS_READ
        )
        for value in asset_owners:
            key, name, _, _ = value
            __ASSET_OWNERS[name] = key
            if name == 'UNKNOWN':
                __UNKNOWN_KEY = key

def asset_owner_to_key(asset_owner):
    """ Convert dollar value ranges to storage keys
    Args:
        asset_owner: str - "Joint" Describes which account
            an asset is owned by (Self, Child, Spouse)
    """
    __fetch_asset_owners()
    if asset_owner in __ASSET_OWNERS:
        return __ASSET_OWNERS[asset_owner]

    return __UNKNOWN_KEY
