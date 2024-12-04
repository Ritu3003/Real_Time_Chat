from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message

@login_required
def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages
    })
