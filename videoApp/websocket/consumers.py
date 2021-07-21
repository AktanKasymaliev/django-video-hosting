import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from videoApp.models import Comments


class CommentsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.video_id = self.scope["url_route"]["kwargs"]["video_id"]

        self.video_group_name = f"video_{self.video_id}"
        # Join room group
        await self.channel_layer.group_add(
            self.video_group_name,
            self.channel_name
        )

    async def disconnect(self, code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.video_group_name,
            self.channel_name
        )

    # Receive message from web socket
    async def receive(self, text_data, bytes_data):

        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await self.save_comment(username, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.video_group_name,
            {
                'type': 'new_comment',
                'message': message,
                'username': username
            }
        )

    
    # Receive message from room group
    async def new_comment(self, event):
        message = event['message']
        username = event["username"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_comment(self, username, message):
        Comments.objects.create(
            username=username, 
            message=message,
            video=self.video_id
            )
