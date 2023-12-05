from django.urls import path
from . import views


urlpatterns = [
    path("api/rooms/", views.room_list, name="room_list"),
    path("api/rooms/<int:room_id>/", views.room_detail, name="room_detail"),
]


