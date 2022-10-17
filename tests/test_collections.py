from unittest import TestCase
import pytest
from collections_local.count_ import count_items_in_a_list
from collections_local.count_ import count_most_common_in_object
from collections_local.namedtuple_ import create_object, build_coordinates_object


class CountTest(TestCase):

    def setUp(self) -> None:
        self.test_list = [1, 1, 2, 2, 3, 3, 3]

    def test_count_items_in_a_list(self):
        self.assertEqual(count_items_in_a_list(self.test_list), {1: 2, 2: 2, 3: 3})

    def test_count_most_common_in_object(self):
        self.assertEqual(count_most_common_in_object(self.test_list), 3)


class NamedTupleTest(TestCase):

    def setUp(self) -> None:
        self.object_name = 'Animal'
        self.attributes = 'name owner age'
        Animal = create_object(self.object_name, self.attributes)
        self.animal = Animal('bob', 'steve', 12)

    def test_valida_create_object_attribute(self):
        self.assertEqual(self.animal.age, 12)


# Pytest

def test_count_items_in_a_list():
    assert count_items_in_a_list([1, 1, 2, 2, 3, 3, 3]) == {1: 2, 2: 2, 3: 3}


def test_count_most_common_in_object():
    assert count_most_common_in_object([1, 1, 2, 2, 3, 3, 3]) == 3


