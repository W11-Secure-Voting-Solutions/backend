from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.postgres import fields


class BulletinBoard:
  election = models.ForeignKey('helios.Election', on_delete=models.CASCADE)
  content = fields.JSONField(default={})

  @classmethod
  def create_for_election(cls, election):
    return cls(election=election, content={})
