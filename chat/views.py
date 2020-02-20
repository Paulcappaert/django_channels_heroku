# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import ChatRoom, ChatMessage

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    room, _ = ChatRoom.objects.get_or_create(name=room_name)
    messages = room.messages.all().values_list('content', flat=True)[:10]
    messages = list(map(json.dumps, messages))
    messages = list(map(mark_safe, messages))
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': messages,
    })