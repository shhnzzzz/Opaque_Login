import hashlib
import secrets
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_SECRET = int(os.getenv("SERVER_SECRET"))

PRIME = 2**255 - 19



def hash_password(password: str) -> int:
    digest = hashlib.sha256(password.encode()).digest()
    return int.from_bytes(digest, "big") % PRIME


def blind(password: str):
    point = hash_password(password)

    blind_factor = secrets.randbelow(PRIME - 1) + 1

    blinded = (point * blind_factor) % PRIME

    return blinded, blind_factor


def evaluate(blinded: int):
    return (SERVER_SECRET * blinded) % PRIME


def unblind(evaluated: int, blind_factor: int):

    inverse = pow(blind_factor, -1, PRIME)

    return (evaluated * inverse) % PRIME

