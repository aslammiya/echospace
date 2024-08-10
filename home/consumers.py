from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import *
from channels.db import database_sync_to_async


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomName = self.scope['url_route']['kwargs']['roomname']       
        await self.channel_layer.group_add(
            self.roomName,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        data = json.loads(text_data)
        msg = data['msg']
        userName = data['username']
        userProfileImage = data['userProfileImage']
        timeString = data['timeString']
        await self.channel_layer.group_send(
            self.roomName,
            {
                'type': 'chat_message',
                'timeString': timeString,
                'message': msg,
                'username': userName,
                'userProfileImage': userProfileImage
            }
        )

    async def chat_message(self, event):
        print("Event...", event)
        msg = event['message']
        userName = event['username']
        userProfileImage = event['userProfileImage']
        timeString = event['timeString']
        await self.send(text_data=json.dumps({
            'timeString': timeString,
            'msg': msg,
            'username': userName,
            'userProfileImage': userProfileImage
        }))

    async def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)