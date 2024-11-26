import smtplib
import unittest
import mockito
import pytest

from julklap.group import Group
from julklap.person import Person
from julklap.exceptions import NoPossibleJulklapMappingError
from julklap.email_connector import EmailConnector


class TestEmailConnector(unittest.TestCase):
    """
    Test the EmailConnector class.
    """

    def test_init(self):
        """
        Test init functions of the EmailConnector class.
        """
        # Test basic param setting
        connector = EmailConnector(
            "jean@gmail.com",
            "password"
        )
        self.assertEqual(connector.sender_address, "jean@gmail.com")
        self.assertEqual(connector.sender_password, "password")
        self.assertEqual(connector.session, None)

    def test_enter_exit(self):
        """
        Test __enter__, __exit__ functions of the EmailConnector class.
        """
        # Test basic param setting
        connector = EmailConnector(
            "jean@gmail.com",
            "password"
        )
        mockito.expect(smtplib.SMTP, times=1).starttls()
        mockito.expect(smtplib.SMTP, times=1).login("jean@gmail.com", "password")
        mockito.expect(smtplib.SMTP, times=1).quit()
        with connector as c:
            self.assertNotEqual(c.session, None)
        self.assertEqual(connector.session, None)
        mockito.verifyNoUnwantedInteractions()
        mockito.unstub()

    def test_send_email(self):
        """
        Test send_email function of the EmailConnector class.
        """
        # Test basic param setting
        santa = Person("Santa Claus", "santa@claus.de")
        kid = Person("Kiddo", "dad@work.com")
        kid2 = Person("Alfred", "dad@work.com")
        connector = EmailConnector(
            "jean@gmail.com",
            "password"
        )
        mockito.expect(smtplib.SMTP, times=1).starttls()
        mockito.expect(smtplib.SMTP, times=1).login("jean@gmail.com", "password")
        mockito.expect(smtplib.SMTP, times=1).quit()
        mockito.expect(smtplib.SMTP, times=1).sendmail(
            "jean@gmail.com", "santa@claus.de",
            mockito.matchers.arg_that(lambda mime: "Kiddo" in mime)
        )
        mockito.expect(smtplib.SMTP, times=1).sendmail(
            "jean@gmail.com", "santa@claus.de",
            mockito.matchers.arg_that(lambda mime: "Alfred" in mime)
        )
        with connector as c:
            c.send_email(santa, kid)
            c.send_email(santa, kid2)
        mockito.verifyNoUnwantedInteractions()
        mockito.unstub()
