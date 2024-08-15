from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import *
import redis
import json

class WebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['roomname']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope['user'].username

        # try:
        #     self.userProfileImage = self.scope['user'].profile_image.url
        # except Exception:
        #     self.userProfileImage = 'guest_image'        

        # Initialize Redis client with a Redis URL
        # redis_client = redis.Redis(host='localhost', port=6379, db=0)

        # Store the username and profile image in Redis
        # user_data = json.dumps({
        #     'username': self.username,
        #     'userProfileImage': self.userProfileImage
        # })
        # redis_client.set(f"user_data:{self.channel_name}", user_data)

        # # Add the channel to the room's channel list
        # redis_client.lpush(f'channels:{self.room_group_name}', self.channel_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Retrieve all user data from the room
        # channels = redis_client.lrange(f'channels:{self.room_group_name}', 0, -1)
        # users = []
        # for channel in channels:
        #     user_data = redis_client.get(f"user_data:{channel.decode('utf-8')}")
        #     if user_data:
        #         users.append(json.loads(user_data))

        # Send the list of users to the room
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'join_message',
        #         'username': self.username,
        #         'userProfileImage': self.userProfileImage
        #         # 'users': users,
        #     }
        # )

        await self.accept()

    async def receive_json(self, content):
        print("Message received from client...", content)
        
        # Extract message data
        self.msg = content.get('msg')
        self.user_name = content.get('username')
        self.user_profile_image = content.get('userProfileImage')
        self.time_string = content.get('timeString')
        command = content.get('command')

        if command == 'join_room':
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            print('Added to room:', self.room_group_name)
        
        elif command == 'message':
            print('Sending message')
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'timeString': self.time_string,
                    'message': self.msg,
                    'username': self.user_name,
                    'userProfileImage': self.user_profile_image
                }
            )
            print('Message sent')        
        
        
        elif command == 'join':
            print('Join msg call', self.user_name, self.user_profile_image)
            # users = await self.get_users_in_group()
            # print(users)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'join.message',
                    'username':self.user_name,
                    'userProfileImage':self.user_profile_image
                    # 'users':users
                }
            )

        elif command == 'offer':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'offer.message',
                    'offer': content.get('offer')
                }
            )

        elif command == 'answer':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'answer.message',
                    'answer': content.get('answer')
                }
            )

        elif command == 'candidate':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'candidate.message',
                    'candidate': content.get('candidate'),
                    'iscreated': content.get('iscreated')
                }
            )
        else:
            print("Unknown command:", command)

    async def chat_message(self, event):
        await self.send_json({
            'type': 'chat_message',
            'timeString': event['timeString'],
            'message': event['message'],
            'username': event['username'],
            'userProfileImage': event['userProfileImage']
        })

    async def join_message(self, event):
        print('Join msg func call ',event)
        await self.send_json({
            'type': 'join_message',
            'username': event['username'],
            'userProfileImage': event['userProfileImage']
            # 'users': event.get('users', [])
        })

    # async def chat_message(self, event):
    #     print("Event...", event)
    #     msg = event['message']
    #     userName = event['username']
    #     userProfileImage = event['userProfileImage']
    #     timeString = event['timeString']
    #     await self.send_json({
    #         'timeString': timeString,
    #         'msg': msg,
    #         'username': userName,
    #         'userProfileImage': userProfileImage
    #     })

    async def offer_message(self,event):
        await self.send_json({
            'command':'offer',
            'offer':event['offer']
        })
    
    async def answer_message(self,event):
        await self.send_json({
            'command':'answer',
            'answer':event['answer']
        })
    
    async def candidate_message(self,event):
        await self.send_json({
            'command':'candidate',
            'candidate':event['candidate'],
            'iscreated':event['iscreated']
        })
        
    async def disconnect(self, close_code):
        # redis_client = redis.Redis(host='localhost', port=6379, db=0)

        # # Remove user data from Redis
        # redis_client.delete(f"user_data:{self.channel_name}")
        # redis_client.lrem(f'channels:{self.room_group_name}', 0, self.channel_name)

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def get_users_in_group(self):
        # Initialize Redis client with the same Redis URL
        redis_client = redis.Redis(host='localhost', port=6379, db=0)

        # Fetch all channels in the group
        channels = redis_client.lrange(f'channels:{self.room_group_name}', 0, -1)

        # Fetch associated user data for each channel
        users = []
        for channel in channels:
            user_data = redis_client.get(channel)
            
            if not user_data:
                print(f"No data found for channel: {channel}")
                continue
            
            try:
                user_info = json.loads(user_data.decode('utf-8'))
                users.append(user_info)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for channel: {channel}, data: {user_data}")
                continue
        
        return users
