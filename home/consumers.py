from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class WebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['roomname']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope['user'].username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content):
        print("Message received from client...", content)
        
        command = content.get('command')
        if command == 'message':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': content.get('msg'),
                    'username': content.get('username'),
                    'userProfileImage': content.get('userProfileImage'),
                    'timeString': content.get('timeString')
                }
            )
        elif command == 'join':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'join_message',
                    'username': content.get('username'),
                    'userProfileImage': content.get('userProfileImage')
                }
            )
        elif command == 'offer':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'offer',
                    'offer': content.get('offer'),
                    'room': content.get('room'),
                }
            )
        elif command == 'answer':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'answer',
                    'answer': content.get('answer'),
                    'room': content.get('room'),
                }
            )
        elif command == 'candidate':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'candidate',
                    'candidate': content.get('candidate'),
                    'isCreated': content.get('isCreated'),
                    'room': content.get('room'),
                }
            )

    async def chat_message(self, event):
        await self.send_json({
            'type': 'chat_message',
            'message': event['message'],
            'username': event['username'],
            'userProfileImage': event['userProfileImage'],
            'timeString': event['timeString']
        })

    async def join_message(self, event):
        await self.send_json({
            'type': 'join_message',
            'username': event['username'],
            'userProfileImage': event['userProfileImage']
        })

    async def offer(self, event):
        await self.send_json({
            'command': 'offer',
            'offer': event['offer'],
            'room': event['room'],
        })

    async def answer(self, event):
        await self.send_json({
            'command': 'answer',
            'answer': event['answer'],
            'room': event['room'],
        })

    async def candidate(self, event):
        await self.send_json({
            'command': 'candidate',
            'candidate': event['candidate'],
            'isCreated': event['isCreated'],
            'room': event['room'],
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
