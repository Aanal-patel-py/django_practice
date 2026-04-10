from channels.generic.websocket import AsyncWebsocketConsumer #AsyncWebsocketConsumer → a base class provided by Channels to handle WebSocket connections asynchronously.By inheriting from it, you get methods like connect, receive, disconnect, which you can override.
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self): #automatically called when a browser/client opens a WebSocket connection.
        await self.accept()  # tells Channels to accept the connection. If you don’t call this, the connection is rejected.
        await self.send(text_data="Hello from server!")

    async def receive(self, text_data): #called every time the client sends a message.
        await self.send(text_data=text_data) #sends the same message back to the client.

class Notify(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name='users_123'
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name

        )
        print(f"channel name: {self.channel_name}")
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        data=json.loads(text_data)
        
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "notify.msg" ,
                "message":data.get("message")
            }
        )

    async def notify_msg(self,event):
        await self.send(
            text_data=json.dumps({
                "message": event["message"]
            }
            )
        )