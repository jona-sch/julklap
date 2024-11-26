import unittest
import mockito
import pytest

from julklap.group import Group
from julklap.person import Person
from julklap.exceptions import NoPossibleJulklapMappingError
from julklap.julklap import Julklap
from julklap.email_connector import EmailConnector


class TestJulklap(unittest.TestCase):
    """
    Test the Julklap class.
    """

    def test_julklap(self):
        """
        Test init functions of the Person class.
        """
        # Test basic param setting
        p1 = Person("1Jean", "jean@gmail.com")
        p2 = Person("2Jacques", "jacques@gmail.com")
        p3 = Person("3Julien", "julien@gmail.com")
        p4 = Person("4Jerome", "jerome@gmail.com")
        p5 = Person("5Jan", "jan@gmail.com")
        group = Group(
            {p1, p2, p3, p4, p5}, [[p1, p3], [p1, p4], [p2, p4], [p2, p5], [p3, p5]]
        )
        # these exclusion guarantee that the only solution is p1->p2->p3->p4->p5
        # or p5->p4->p3->p2->p1->p5
        email_connector = mockito.mock(EmailConnector)
        mockito.expect(email_connector, times=1).__enter__(...).thenReturn(
            email_connector
        )
        for m1, m2 in [[p1, p2], [p2, p3], [p3, p4], [p4, p5], [p5, p1]]:
            mockito.expect(email_connector, times=1).send_email(
                mockito.matchers.or_(m1, m2), mockito.matchers.or_(m1, m2)
            )
        mockito.expect(email_connector, times=1).__exit__(...)

        julklap = Julklap(group, email_connector)
        julklap.compute_julklap()
        mockito.verifyNoUnwantedInteractions()
