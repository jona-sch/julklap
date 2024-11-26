import logging
import random as rd
from julklap.julklap import Julklap
from input_vars import *
from julklap.email_connector import EmailConnector


rd.seed()

if __name__ == "__main__":
    logging.getLogger(__name__).info("Processing input variables...")
    group = Group(persons, exclusions)
    email_connector = EmailConnector(sender_email, sender_password)
    julklap = Julklap(group, email_connector)

    logging.getLogger(__name__).info("Computing Julklap matching and sending emails...")
    julklap.compute_julklap()

    logging.getLogger(__name__).info("All done.")
