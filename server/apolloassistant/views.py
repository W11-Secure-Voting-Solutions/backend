from django.shortcuts import render

from helios.view_utils import (
    return_json
)
from helios.models import (
    Voter,
)
# Create your views here.

def fail_response(message):
  return {
    "status": "fail",
    "message": message,
  }

def success_response(message, data=None):
  return {
    "status": "success",
    "message": message,
    "data": data or {}
  }



@return_json
def get_bulletin_board(request):

  session_id = request.GET.get('session_id')

  if not session_id:
    return fail_response("Please provide session_id as GET param.")

  voter = Voter.objects.filter(session_id=session_id).first()

  if not voter:
    return fail_response("session_id '%s' is invalid" % session_id)

  return success_response("Success. To be implemented: return bulletin board.")
