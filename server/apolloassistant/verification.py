import pathlib

from django.conf import settings

import functools

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA


@functools.lru_cache()
def get_rsa_privkey():
    return RSA.importKey(settings.RSA_PRIVATE_KEY.encode())


@functools.lru_cache()
def get_rsa_pubkey():
    return RSA.importKey(settings.RSA_PUBLIC_KEY.encode())


def hash_msg(message: str) -> bytes:
    h = SHA.new()
    h.update(message.encode())
    return h


def sign(message: str):
    signer = PKCS1_PSS.new(get_rsa_privkey())
    h = hash_msg(message)
    signature = signer.sign(h)
    return signature


def verify(message, signature) -> bool:
    verifier = PKCS1_PSS.new(get_rsa_pubkey())
    h = hash_msg(message)
    return verifier.verify(h, signature)
