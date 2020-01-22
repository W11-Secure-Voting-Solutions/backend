from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from helios.models import FakeBooth
from helios.serializers import FakeBoothSerializer


class FakeBoothViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):

    queryset = FakeBooth.objects.all()
    serializer_class = FakeBoothSerializer

    def update(self, request, pk=None):
        booth, _ = FakeBooth.objects.get_or_create(id=pk,
                                                   defaults={"body": []})
        booth.body.append(request.data)
        booth.save()
        return Response(status=status.HTTP_200_OK)
