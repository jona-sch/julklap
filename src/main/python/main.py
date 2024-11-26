import logging
import random as rd
from julklap.julklap import Julklap
from julklap.email_connector import EmailConnector
from julklap.group import Group
from input_vars import persons, exclusions, sender_email, sender_password


rd.seed()

if __name__ == "__main__":
    logging.getLogger(__name__).info("Processing input variables...")
    group = Group(persons, exclusions)
    email_connector = EmailConnector(sender_email, sender_password)
    julklap = Julklap(group, email_connector)

    logging.getLogger(__name__).info("Computing Julklap matching and sending emails...")
    julklap.compute_julklap()

    logging.getLogger(__name__).info("All done.")
