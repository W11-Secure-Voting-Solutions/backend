from rest_framework import serializers

from helios.models import FakeBooth


class FakeBoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeBooth
        fields = ("created_at", "updated_at", "body")
        read_only_fields = ("created_at", "updated_at")
