from unittest import TestCase
import pytest
from collections_local.defaultdict_ import count_items_by_name, group_items_by_name, group_unique_items


class DefaultDictTest(TestCase):

    def setUp(self) -> None:
        self.test_data_unique = [('Sales', 'John Doe'),
                                 ('Sales', 'Martin Smith'),
                                 ('Accounting', 'Jane Doe'),
                                 ('Marketing', 'Elizabeth Smith'),
                                 ('Marketing', 'Adam Doe')]

        self.test_data_with_duplicates = [('Sales', 'John Doe'),
                                          ('Sales', 'Martin Smith'),
                                          ('Accounting', 'Jane Doe'),
                                          ('Marketing', 'Elizabeth Smith'),
                                          ('Marketing', 'Elizabeth Smith'),
                                          ('Marketing', 'Adam Doe'),
                                          ('Marketing', 'Adam Doe'),
                                          ('Marketing', 'Adam Doe')]

    def test_count_items_by_name(self):
        should_be = {'Sales': ['John Doe', 'Martin Smith'],
                     'Accounting': ['Jane Doe'],
                     'Marketing': ['Elizabeth Smith', 'Adam Doe']}
        self.assertEqual(group_items_by_name(self.test_data_unique), should_be)

    def test_group_unique_items(self):
        should_be = {'Sales': {'John Doe', 'Martin Smith'}, 'Accounting': {'Jane Doe'},
                     'Marketing': {'Adam Doe', 'Elizabeth Smith'}}
        self.assertEqual(group_unique_items(self.test_data_with_duplicates), should_be)

    def test_count_items_by_name(self):
        should_be = {'Sales': 2, 'Accounting': 1, 'Marketing': 2}
        self.assertEqual(count_items_by_name(self.test_data_unique), should_be)


