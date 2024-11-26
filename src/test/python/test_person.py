import unittest
import pytest

from julklap.person import Person


class TestPerson(unittest.TestCase):
    """
    Test the Person class.
    """

    def test_init(self):
        """
        Test init functions of the Person class.
        """
        # Test basic param setting
        person = Person("Jean", "jean@gmail.com")
        self.assertEqual(person.name, "Jean")
        self.assertEqual(person.email, "jean@gmail.com")
        # Test bad email address
        with self.assertRaises(ValueError):
            Person("Jean", "jeangmail.com")
        # Test empty name
        with self.assertRaises(ValueError):
            Person("", "jean@gmail.com")

    def test_eq(self):
        """
        Test eq function of the Person class.
        """
        # Test eq
        person1 = Person("Jean", "jean@gmail.com")
        person2 = Person("Jean", "jean2@gmail.com")
        self.assertEqual(person1, person2)
        # Test neq
        person1 = Person("Jean", "jean@gmail.com")
        person2 = Person("Jacques", "jacques@gmail.com")
        self.assertNotEqual(person1, person2)
