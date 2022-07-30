from django.db import models
from datetime import time


# Create your models here.
class Room(models.Model):
    name_room = models.CharField(max_length=25)
    floor = models.IntegerField()
    number_of_room = models.IntegerField()

    def __str__(self):
        return f"The room : {self.name_room} of floor : {self.floor} and number {self.number_of_room}"


class Meeting(models.Model):
    title_meeting = models.CharField(max_length=200)
    duration = models.TimeField(default=time(1))
    start_time = models.TimeField(default=time(9))
    date_meeting = models.DateField()
    room = models.ForeignKey(Room,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title_meeting} in {self.date_meeting} at {self.title_meeting}"

