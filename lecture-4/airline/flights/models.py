from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code}, {self.city}"

class Flight(models.Model):
    # related_name allows you to acces a relationship in the reverse order
    # with the FK, I can do origin.Airport, with related_name="departures" 
    # I can do airport.departures
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.origin}, {self.destination}, {self.duration}"
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # allows flight.passengers with the related_name
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"