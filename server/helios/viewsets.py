from rest_framework import viewsets, mixins

from helios.models import FakeBooth
from helios.serializers import FakeBoothSerializer


class FakeBoothViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):

    queryset = FakeBooth.objects.all()
    serializer_class = FakeBoothSerializer


