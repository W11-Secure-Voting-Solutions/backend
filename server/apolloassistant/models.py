from typing import Sequence

from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.postgres import fields

from helios.models import Election
from helios_auth.models import User

NUM_OF_CAST_CODES = 10
LOCKIN_CODE_LENGTH = 8
CAST_CODE_LENGTH = 8


def _generate_lockin_code() -> str:
    return get_random_string(LOCKIN_CODE_LENGTH)


def _generate_cast_code() -> str:
    return get_random_string(CAST_CODE_LENGTH)


class CastCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    value = models.TextField(unique=True, default=_generate_cast_code)
    used = models.BooleanField(default=False)

    @classmethod
    def create_for_election(cls, user: User, election: Election) -> None:
        cls.objects.bulk_create(
            [cls(user=user, election=election) for _ in range(NUM_OF_CAST_CODES)]
        )


class LockInCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    value = models.TextField(unique=True, default=_generate_lockin_code)
    used = models.BooleanField(default=False)

    @classmethod
    def create_for_election(cls, user: User, election: Election) -> None:
        cls.objects.create(user=user, election=election)
