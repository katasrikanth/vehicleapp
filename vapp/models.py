from django.db import models
from django.urls import reverse

class Vehicle(models.Model):
    vehiclename = models.CharField(max_length=100)
    speed = models.FloatField(null=True, blank=True) 
    avgspeed = models.FloatField(null=True,blank=True)
    Temperature = models.FloatField(null=True,blank=True)
    fuellevel = models.FloatField(null=True,blank=True)
    enginestats = models.FloatField(null=True,blank=True)
    image1 = models.ImageField(upload_to='vehicleimg/image1')
    image2 = models.ImageField(upload_to='vehicleimg/image2')

    def __str__(self):
        return self.vehiclename

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])