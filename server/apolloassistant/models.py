from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.postgres import fields


class AssistantSession(models.Model):
    user = models.ForeignKey('helios_auth.User', on_delete=models.CASCADE)
    election = models.ForeignKey('helios.Election', on_delete=models.CASCADE)
    session_title = models.TextField(max_length=50, default='')
    session_id = models.TextField(default='')
    secret_key = models.TextField(default='')
