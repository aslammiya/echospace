from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import *

class WebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.roomName = self.scope['url_route']['kwargs']['roomname']       
        await self.channel_layer.group_add(
            self.roomName,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content):
        print("Message received from client...", content)
        msg = content['msg']
        userName = content['username']
        userProfileImage = content['userProfileImage']
        timeString = content['timeString']
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
        await self.send_json({
            'timeString': timeString,
            'msg': msg,
            'username': userName,
            'userProfileImage': userProfileImage
        })

    async def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)
