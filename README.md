# JULKLAP

This is a cleaned-up version of some code I had laying around.

It allows you to generate a Julklap (Secret Santa) among a group of friends.

## Functionnalities

- Run a Secret Santa among a group of people.
- Mutual exclusions between participants: exclude couples from offering each other gifts.

## Limitations

- For now, only single-chain mappings are possible (p1->p2->...p_n->p1). This eliminates some possibilities, so you can't have too many exclusions.
- Input variables must be set using the Python input file `src/main/python/input_vars.py`.
- Only works with Gmail sender address (sender address = email address used to send all the e-mails).

## How it works

1. You need to decide on a GMail sender address.
2. Generate an app password (look it up).
3. Set all your input vars in the `src/main/python/input_vars.py` file.
4. Execute `python src/main/python/main.py`
5. That's it !

## Dev

You will need a virtualenv where you will install the `dev-requirements.txt`.

### UT

For UTs, you should first `export PYTHONATH=src/main/python`.
They are based on pytest, simply run `pytest`.

### Linting

No lint checking is implemented, but `black` auto-formatter is used.

### Typing

TODO.

### TODO

- Allow better input of variables through files.
- Allow other types of mapping than single-chain (see limitations): graph theory.
- Add mypy type testing.
- Don't be dependant on GMail (test other email providers).
