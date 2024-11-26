from dataclasses import dataclass, field
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from typing import Final, Optional

from julklap.utils import validate_email_address
from julklap.person import Person


@dataclass
class EmailConnector:
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

    session: Optional[smtplib.SMTP] = field(default=None)

    message: Final[
        str
    ] = """Hallo/Bonjour/Hej PLACEHOLDER_SDR,

You have to make a gift to PLACEHOLDER_RCV.
This email was sent with the help of the smtplib library.
Checkout the GitHub repo: github.com/link/to/repo.

Have a good day."""

    subject: Final[str] = "JULKLAP - Confidential"

    def __post_init__(self):
        if not validate_email_address(self.sender_address):
            raise ValueError(f"Entered e-mail is not correct: {self.sender_address}")

    def __enter__(self) -> "EmailConnector":
        self.session = smtplib.SMTP("smtp.gmail.com", 587)
        self.session.starttls()
        self.session.login(self.sender_address, self.sender_password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.quit()
        self.session = None

    def send_email(self, person: Person, gifted_person: Person) -> None:
        """
        Send the Julklap email to a Person.

        Args:
            person (Person): the Person we want to send the email to.
        """
        message = MIMEMultipart()
        message["From"] = self.sender_address
        message["To"] = person.email
        message["Subject"] = self.subject
        message.attach(
            MIMEText(self.message.replace("PLACEHOLDER_RCV", gifted_person.name).replace("PLACEHOLDER_SDR", person.name), "plain")
        )
        self.session.sendmail(self.sender_address, person.email, message.as_string())
