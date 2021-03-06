""" Test cases for dollar_value singleton """

from unittest import TestCase

from src.store.entities.dollar_value import dollar_value_to_key
from src.store.sql import DOLLAR_VALUE_DEFAULTS

class TestDollarValue(TestCase):
    """ Ensure defaults and accurate key fetching """

    def test_simple_get(self):
        """ Single key by name """
        unknown_key = dollar_value_to_key('UNKNOWN')
        self.assertNotEqual(
            dollar_value_to_key('$50,001 - $100,000'),
            unknown_key)

    def test_unknown_default(self):
        """ Key misses mean Unknown """
        unknown_key = dollar_value_to_key('UNKNOWN')
        self.assertGreater(unknown_key, 0)
        self.assertEqual(
            unknown_key,
            dollar_value_to_key('HEY THIS ISNT A REAL KEY'))
        self.assertEqual(
            unknown_key,
            dollar_value_to_key('Unascertainable'))
        self.assertEqual(
            unknown_key,
            dollar_value_to_key(''))
        self.assertEqual(
            unknown_key,
            dollar_value_to_key(None))

    def test_defaults(self):
        """ Ensure all defaults """
        for default in DOLLAR_VALUE_DEFAULTS:
            self.assertGreater(
                dollar_value_to_key(default['value_name']),
                0)

    def test_remap_to_one_million(self):
        """ Ensure remapping occurs """
        one_million_range = dollar_value_to_key('$1,000,001 - $5,000,000')
        other_million_plus = dollar_value_to_key(
            'Over $1,000,000 and held independently by spouse or dependent child')
        self.assertEqual(one_million_range, other_million_plus)
