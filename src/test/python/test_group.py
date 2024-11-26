import unittest
import pytest

from julklap.group import Group
from julklap.person import Person
from julklap.exceptions import NoPossibleJulklapMappingError


class TestGroup(unittest.TestCase):
    """
    Test the Group class.
    """

    def setUp(self):
        self.p1 = Person("1Jean", "jean@gmail.com")
        self.p2 = Person("2Jacques", "jacques@gmail.com")
        self.p3 = Person("3Julien", "julien@gmail.com")
        self.p4 = Person("4Jerome", "jerome@gmail.com")
        self.p5 = Person("5Jan", "jan@gmail.com")

    def test_init_and_add_person(self):
        """
        Test init functions of the Person class.
        """
        # Test basic param setting
        group = Group({self.p1, self.p2}, [[self.p1, self.p2]])
        self.assertEqual(group.name, "People Group")
        self.assertEqual(group.people, {self.p1, self.p2})
        self.assertEqual(group.exclusions, [[self.p1, self.p2]])
        # Add a Person
        group.add_person(self.p3)
        self.assertEqual(group.people, {self.p1, self.p2, self.p3})
        group.add_person(self.p1)
        self.assertEqual(group.people, {self.p1, self.p2, self.p3})

    def test_create_matches_errors(self):
        """
        Test eq function of the Person class.
        """
        # Too many exclusions
        group = Group({self.p1, self.p2}, [[self.p1, self.p2]])
        with self.assertRaises(NoPossibleJulklapMappingError):
            group.create_matches()
        # Too little people
        group = Group({self.p1})
        with self.assertRaises(NoPossibleJulklapMappingError):
            group.create_matches()

    def test_create_matches_no_exclusions(self):
        """
        Test create matches w/o exclusions.
        """
        # 2 people
        group = Group({self.p1, self.p2})
        matches = group.create_matches()
        self.assertIn((self.p1, self.p2), matches)
        self.assertIn((self.p2, self.p1), matches)
        self.assertEqual(2, len(matches))
        # 5 people
        group = Group({self.p1, self.p2, self.p3, self.p4, self.p5})
        matches = group.create_matches()
        self._validate_matches(matches, group)
        # Do it a few times
        matches = group.create_matches()
        self._validate_matches(matches, group)
        matches = group.create_matches()
        self._validate_matches(matches, group)
        matches = group.create_matches()
        self._validate_matches(matches, group)

    def test_create_matches_with_exclusions(self):
        """
        Test create matches w/ exclusions.
        """
        # 5 people
        group = Group(
            {self.p1, self.p2, self.p3, self.p4, self.p5},
            [(self.p1, self.p2), (self.p1, self.p3), (self.p4, self.p5)]
        )
        matches = group.create_matches()
        self._validate_matches(matches, group)
        # Do it a few times
        matches = group.create_matches()
        self._validate_matches(matches, group)
        matches = group.create_matches()
        self._validate_matches(matches, group)
        matches = group.create_matches()
        self._validate_matches(matches, group)
        # 5 people
        group = Group(
            {self.p1, self.p2, self.p3, self.p4, self.p5},
            [(self.p1, self.p2), (self.p2, self.p3), (self.p4, self.p3), (self.p4, self.p5)]
        )
        matches = group.create_matches()
        print(matches)
        self._validate_matches(matches, group)

    def _validate_matches(self, matches, group):
        """
        Validate a match result from the Group class.
        """
        self.assertEqual(len(matches), group.number_of_people)
        self.assertSetEqual(set(m[0] for m in matches), group.people)
        self.assertSetEqual(set(m[1] for m in matches), group.people)
        self.assertTrue(all(m[0] != m[1] for m in matches))
        self.assertTrue(all(all({m0, m1} != {p1, p2} for m0, m1 in matches) for p1, p2 in group.exclusions))
