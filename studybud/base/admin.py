from django.contrib import admin
from .models import Room, RoomDetail



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(RoomDetail)
class RoomDetailAdmin(admin.ModelAdmin):
    list_display = ["room", "description"]



