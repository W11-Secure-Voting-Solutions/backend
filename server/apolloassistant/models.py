from typing import Sequence

from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.postgres import fields

NUM_OF_CAST_CODES = 10
LOCKIN_CODE_LENGTH = 8
CAST_CODE_LENGTH = 8


def _generate_lockin_code() -> str:
    return get_random_string(LOCKIN_CODE_LENGTH)


def _generate_cast_code() -> str:
    return get_random_string(CAST_CODE_LENGTH)


class CastCode(models.Model):
    session_id = models.TextField(unique=True)
    value = models.TextField(unique=True, default=_generate_cast_code)
    used = models.BooleanField(default=False)

    @classmethod
    def create_for_session(cls, session_id: str) -> None:
        cls.bulk_create(
            [cls(session_id=session_id) for _ in range(NUM_OF_CAST_CODES)])


class LockInCode(models.Model):
    session_id = models.TextField(unique=True)
    value = models.TextField(unique=True, default=_generate_lockin_code)
    used = models.BooleanField(default=False)

    @classmethod
    def create_for_session(cls, session_id: str) -> None:
        cls.objects.create(session_id=session_id)
