from dataclasses import dataclass

from pydantic import BaseModel

from julklap.utils import validate_email_address
from julklap.email_connector import EmailConnector


@dataclass
class EmailConnectorModel(BaseModel):
    """
    EmailConnector class. It is used to send emails to the people.
    Usage:
    ```
    with EmailConnector("sender@address.com", "password") as conn:
        conn.send_email(personA, personB)
    ```
    """

    sender_address: str
    """Sender address that will be used."""

    sender_password: str
    """Sender password that will be used."""

    def __post_init__(self):
        if not validate_email_address(self.sender_address):
            raise ValueError(f"Entered e-mail is not correct: {self.sender_address}")

    def create_email_connector(self) -> EmailConnector:
        return EmailConnector(
            sender_address=self.sender_address,
            sender_password=self.sender_password
        )
