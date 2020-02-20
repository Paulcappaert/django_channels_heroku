from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=30, unique=True)

class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.CharField(max_length=100)