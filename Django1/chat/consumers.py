from channels.generic.websocket import AsyncWebsocketConsumer #AsyncWebsocketConsumer → a base class provided by Channels to handle WebSocket connections asynchronously.By inheriting from it, you get methods like connect, receive, disconnect, which you can override.
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self): #automatically called when a browser/client opens a WebSocket connection.
        await self.accept()  # tells Channels to accept the connection. If you don’t call this, the connection is rejected.
        await self.send(text_data="Hello from server!")

    async def receive(self, text_data): #called every time the client sends a message.
        # Echo the received message back
        await self.send(text_data=text_data) #sends the same message back to the client.