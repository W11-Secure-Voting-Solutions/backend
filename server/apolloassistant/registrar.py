import logging

from typing import Sequence

from .models import LockInCode
from .models import CastCode


def generate_codes_for_session(session_id: str):
    CastCode.create_for_session(session_id)
    LockInCode.create_for_session(session_id)


def send_email_with_codes(email: str, session_id: str):
    cast_codes = CastCode.objects.filter(session_id=session_id).values_list(
        'value', flat=True)
    lockin_code = LockInCode.objects.get(session_id=session_id).value

    # TODO(szyma): Add email sending here.
    logging.info(
        'Sending email to: %s with cast codes: %s and lockin code: %s' %
        (email, cast_codes, lockin_code))
