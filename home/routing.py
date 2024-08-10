from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ac/room/<str:roomname>/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]
