from django.db import models
from datetime import datetime
from decimal import Decimal

# choice class definition: CharField, and DateTimeField
# function to display question object as string
# function to tell if the question was published recently
class Event(models.Model):
    event_title = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    location = models.CharField(max_length=500)
    registered_users = models.IntegerField(default=0)
    venue_name = models.CharField(max_length=500)
    venue_latitude = models.DecimalField(max_digits=20, decimal_places=3, default=None)
    venue_longitude = models.DecimalField(max_digits=20, decimal_places=3, default=None)
    description = models.CharField(max_length=1000,default="")
    def __str__(self):
        return self.event_title

# EventRatings class definition: ForeignKey, CharField, and IntegerField
# function to display choice object as string
class EventRatings(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    rating = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.comment_text

class EventGroups(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    count_users = models.IntegerField(default=0)

class EventRegistered(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    group = models.ForeignKey(EventGroups, on_delete=models.CASCADE)
