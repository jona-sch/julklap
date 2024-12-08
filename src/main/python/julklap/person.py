from dataclasses import dataclass
import json

from pydantic import BaseModel

from julklap.utils import validate_email_address


@dataclass(frozen=True)
class Person(BaseModel):
    """
    Represents a person: we only need a name and an email address.
    """

    name: str
    """Name of the person. Should not be empty or None."""

    email: str
    """E-mail address. Validated in the post_init."""

    def __post_init__(self):
        if not validate_email_address(self.email):
            raise ValueError(f"Entered e-mail is not correct: {self.email}")
        if self.name == None or self.name == "":
            raise ValueError(f"You should enter a name for your Person.")

    def __eq__(self, other: object) -> bool:
        """Overrides the default implementation"""
        if isinstance(other, Person):
            return self.name == other.name
        return False
