from django.conf.urls import url, include
from apolloassistant import views

urlpatterns = [
    url("pubkey", views.get_registrar_trusted_pubkey),
]
