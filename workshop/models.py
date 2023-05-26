from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    places = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.id)

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    workshop_id = models.ForeignKey('Workshop', null=True, blank=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    content = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
