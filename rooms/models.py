from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = (
        (1, 'Single',
        2, ' Double',
        3, 'Family',
        4, 'Suite'

        )
    )
    name = models.CharField(max_length = 50)
    status = models.CharField(max_length= 30, blank=True)
    room_number = models.IntegerField(blank=True, null=True)
#     room_type = models.PositiveSmallIntegerField(choices=ROOM_TYPES)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
   