from django.conf import settings

from rest_framework import response, decorators, schemas, views


@decorators.api_view()
def get_registrar_trusted_pubkey(request):
    """This endpoint is a secure source of public key of registrar.
    
    It can be used to verify the signature of casted vote with cast code posted
    by the registrar on Bulletin Board after user casts vote.
    """
    return response.Response(settings.RSA_PUBLIC_KEY)
