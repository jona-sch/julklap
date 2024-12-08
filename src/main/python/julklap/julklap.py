from dataclasses import dataclass, field
from datetime import datetime
import logging

from pydantic import BaseModel

from julklap.group import Group
from julklap.email_connector_model import EmailConnectorModel


@dataclass
class Julklap(BaseModel):
    """
    The Julklap main class.
    """

    group: Group
    """Group of people organizing a Julklap event."""

    email_connector_model: EmailConnectorModel
    """The email connector."""

    def compute_julklap(self) -> None:
        """
        Compute a Julklap.
        """
        matches = self.group.create_matches()
        with self.email_connector_model.create_email_connector() as connector:
            for person, gifted_person in matches:
                connector.send_email(person, gifted_person)
