from django.conf.urls import url, include

from apolloassistant import views

urlpatterns = [
    url(r"^bulletinboard$", views.get_bulletin_board),
]