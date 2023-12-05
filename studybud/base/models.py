from django.db import models



class Room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class RoomDetail(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.room.name
    