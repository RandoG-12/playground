from turtle import mode
from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code}\t{self.city}"

class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE) #YUCK!
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.origin}\t{self.destination}\t{self.duration}"