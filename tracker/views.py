from rest_framework import (
    status, 
    viewsets
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from geopy import distance
from geopy.geocoders import Nominatim

from .serializers import (
    HospitalSerializer
)
from .models import (
    Hospital
)


geolocator = Nominatim(user_agent="api-hospital-tracker.herokuapp.com")


# Create your views here.
class ChatbotViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    http_method_names = ['get']

    def list(self, request):
        """
            Lists all hospital from the database via chatbot.

            Returns:
                This returns an array of all hospitals object.
        """
        hospitals = Hospital.objects.all()

        page = self.paginate_queryset(hospitals)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(hospitals, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def find_nearby(self, request):
        """
            Lists all nearby hospital from the database via chatbot.

            Query Params:
                (required) @location: Location for searching nearby hospitals.
                (required) @kilometer: Kilometer distance for searching nearby hospitals.

            Returns:
                This returns an array of nearby hospitals object.

            Raises:
                ValueError: Raises an exception if location param is not provided.
        """
        location = geolocator.geocode(request.GET.get('location'))
        threshold = int(request.GET.get('kilometer'))

        nearest_hospitals_id = []
        hospitals = Hospital.objects.all()
        for hospital in hospitals:
            difference = distance.distance((hospital.lat, hospital.long), (location.latitude, location.longitude)).km
            if difference <= threshold:
                nearest_hospitals_id.append(hospital.id)

        hospitals = Hospital.objects.filter(id__in=nearest_hospitals_id)
        page = self.paginate_queryset(hospitals)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(hospitals, many=True)
        return Response(serializer.data)


class ListHospitalAPIView(ListAPIView):
    """Lists all hospital from the database"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class CreateHospitalAPIView(CreateAPIView):
    """Creates a new hospital"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class UpdateHospitalAPIView(UpdateAPIView):
    """Update the hospital whose id has been passed through the request"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class DeleteHospitalAPIView(DestroyAPIView):
    """Deletes a hospital whose id has been passed through the request"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer