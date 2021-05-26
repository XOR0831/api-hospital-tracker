from django.db import models
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="api-hospital-tracker.herokuapp.com")


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    primary_contact_number = models.CharField(max_length=40, null=True, blank=True)
    secondary_contact_number = models.CharField(max_length=40, null=True, blank=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    icu_beds = models.IntegerField(default=0)
    isolation_beds = models.IntegerField(default=0)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        location = geolocator.geocode(self.address)
        self.lat = location.latitude
        self.long = location.longitude
        return super().save(*args, **kwargs)