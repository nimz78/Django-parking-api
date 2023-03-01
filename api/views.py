from rest_framework import generics

from .models import Parking, ParkingSpace
from .serializers import ParkingSerializer, ParkingSpaceSerializer


class ParkingSpaceList(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer


class ParkingSpaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer


class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


class ParkingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
