from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from .models import *
from channels.db import database_sync_to_async


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket connecteed...")
        print("Channel layer...",self.channel_layer)
        print("Channel layer...",self.channel_name)
        # self.group_name = self.scope['url_route']['kwargs']['group_name']
        # await self.channel_layer.group_add(
        #     self.group_name,
        #     self.channel_name
        # )
        await self.accept() 

    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        # data = json.loads(text_data)
        # print("Data...", data)
        # msg = data['msg']
        # group = await database_sync_to_async(Group.objects.filter(name=self.group_name).first)()
        # chat = Chat(
        #     content = data['msg'],
        #     group = group
        # )
        # await database_sync_to_async(chat.save)()
        # await self.channel_layer.group_send(
        #     self.group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': msg
        #     }
        # )

    # async def chat_message(self, event):
    #     print("Event...", event)
    #     msg = event['message']

    #     await self.send(text_data=json.dumps({
    #         'msg': msg
    #     }))

    async def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)