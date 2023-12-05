from django.core import serializers
from django.http import JsonResponse
from base.models import Room, RoomDetail
import json



def room_list(_request):
    rooms = Room.objects.all()
    room_list = serializers.serialize('json', rooms)
    room_list = json.loads(room_list)  
    return JsonResponse(room_list, safe=False)



def room_detail(_request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        room_detail = RoomDetail.objects.get(room=room)

        data = {
            "id": room.id,
            "name": room.name,
            "description": room_detail.description,
        }

        return JsonResponse(data)
    
    except Room.DoesNotExist:
        return JsonResponse(
            {"error": f"Room with id {room_id} not found"}, status=404
        )
    
    except RoomDetail.DoesNotExist:
        return JsonResponse(
            {"error": f"RoomDetail for Room with id {room_id} not found"}, status=404
        )
    

