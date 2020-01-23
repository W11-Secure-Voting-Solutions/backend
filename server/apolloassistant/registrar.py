import logging

from typing import Sequence

from .models import LockInCode
from .models import CastCode

from helios.models import Election
from helios_auth.models import User
from helios import utils


def generate_codes_for_user_in_election(user: User, election: Election):
    CastCode.objects.filter(user=user, election=election).all().delete()
    LockInCode.objects.filter(user=user, election=election).all().delete()

    CastCode.create_for_election(user, election)
    LockInCode.create_for_election(user, election)


def send_email_with_codes(email: str, election: Election):
    cast_codes = CastCode.objects.filter(election=election).values_list(
        'value', flat=True)
    lockin_code = LockInCode.objects.get(election=election).value
    logging.info('Sending email to: %s with cast codes: %s and '
                 'lockin code: %s for election with UUID: %s' %
                 (email, list(cast_codes), lockin_code, election.uuid))

    sender = 'apollo.votingsystem@gmail.com'
    recipient = [email]
    subject = 'Apollo lock-in and cast codes'
    body = ('Sending email to: %s with cast codes: %s and '
            'lockin code: %s for election with UUID: %s' %
            (email, list(cast_codes), lockin_code, election.uuid))
    utils.send_email(sender, recipient, subject, body)
