from dataclasses import dataclass, field
from datetime import datetime

from julklap.group import Group
from julklap.email_connector import EmailConnector


@dataclass
class Julklap:
    """
    The Julklap main class.
    """

    group: Group
    """Group of people organizing a Julklap event."""

    email_connector: EmailConnector
    """The email connector."""

    def compute_julklap(self) -> None:
        """
        Compute a Julklap.
        """
        matches = self.group.create_matches()
        with self.email_connector as connector:
            for person, gifted_person in matches:
                connector.send_email(person, gifted_person)
