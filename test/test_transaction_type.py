""" Test cases for transaction_type singleton """

from unittest import TestCase

from src.store.entities.transaction_type import transaction_type_to_key
from src.store.sql import TRANSACTION_TYPE_DEFAULTS

class TestTransactionType(TestCase):
    """ Ensure defaults and accurate key fetching """

    def test_simple_get(self):
        """ Single key by name """
        unknown_key = transaction_type_to_key('UNKNOWN')
        self.assertNotEqual(
            transaction_type_to_key('Purchase'),
            unknown_key)

    def test_unknown_default(self):
        """ Key misses mean Unknown """
        unknown_key = transaction_type_to_key('UNKNOWN')
        self.assertGreater(unknown_key, 0)
        self.assertEqual(
            unknown_key,
            transaction_type_to_key('HEY THIS ISNT A REAL KEY'))
        self.assertEqual(
            unknown_key,
            transaction_type_to_key('Unascertainable'))
        self.assertEqual(
            unknown_key,
            transaction_type_to_key(''))
        self.assertEqual(
            unknown_key,
            transaction_type_to_key(None))

    def test_defaults(self):
        """ Ensure all defaults """
        for default in TRANSACTION_TYPE_DEFAULTS:
            self.assertGreater(
                transaction_type_to_key(default['type_name']),
                0)

    def test_remap_sales(self):
        """ Ensure Sale is remapped """
        unknown_key = transaction_type_to_key('UNKNOWN')
        sale_key = transaction_type_to_key('Sale')
        self.assertGreater(sale_key, unknown_key)
        self.assertEqual(
            sale_key,
            transaction_type_to_key('Sale (Full)'))
        self.assertEqual(
            sale_key,
            transaction_type_to_key('Sale (Partial)'))
