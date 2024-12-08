import logging
import random as rd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from julklap.julklap import Julklap
from julklap.exceptions import NoPossibleJulklapMappingError


rd.seed()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def homepage():
    return {"message": "Welcome to the homepage"}


@app.post("/julklap")
def post_julklap(julklap: Julklap):
    logging.getLogger(__name__).info("Computing Julklap matching and sending emails...")
    try:
        julklap.compute_julklap()
    except NoPossibleJulklapMappingError:
        return {"message": "No possible Julklap matchup found for this group."}
    except ValueError as exc:
        return {"message": f"Problem with input: {exc}."}
    logging.getLogger(__name__).info("All done.")
    return {"message": "All done. E-mails have been sent out !"}
