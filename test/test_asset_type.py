""" Test cases for asset_type singleton """

from unittest import TestCase

from src.store.entities.asset_type import asset_type_to_key
from src.store.sql import ASSET_TYPE_DEFAULTS

class TestAssetOwner(TestCase):
    """ Ensure defaults and accurate key fetching """

    def test_simple_get(self):
        """ Single key by name """
        unknown_key = asset_type_to_key('UNKNOWN')
        self.assertNotEqual(
            asset_type_to_key('Deferred Compensation'),
            unknown_key)

    def test_unknown_default(self):
        """ Key misses mean Unknown """
        unknown_key = asset_type_to_key('UNKNOWN')
        self.assertGreater(unknown_key, 0)
        self.assertEqual(
            unknown_key,
            asset_type_to_key('HEY THIS ISNT A REAL KEY'))
        self.assertEqual(
            unknown_key,
            asset_type_to_key('Unascertainable'))
        self.assertEqual(
            unknown_key,
            asset_type_to_key(''))
        self.assertEqual(
            unknown_key,
            asset_type_to_key(None))

    def test_defaults(self):
        """ Ensure all defaults """
        for default in ASSET_TYPE_DEFAULTS:
            self.assertGreater(
                asset_type_to_key(default['type_name']),
                0)
