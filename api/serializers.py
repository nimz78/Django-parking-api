from rest_framework import serializers
from .models import Parking, ParkingSpace


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = (
            "id",
            "name",
            "address",
            "capacity",
        )


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = (
            "id",
            "code",
            "parking",
            "status",
        )
