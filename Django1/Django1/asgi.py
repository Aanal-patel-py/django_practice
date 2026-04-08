"""
ASGI config for Django1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing #Imports your app’s WebSocket URL routing (chat/routing.py) so Channels knows which consumer handles which URL.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django1.settings')

'''application is the entry point for ASGI servers (like Daphne or Uvicorn).
It tells the server:
If this is HTTP → handle with Django’s normal ASGI app
If this is WebSocket → handle with the stack below'''

application = ProtocolTypeRouter({
    'http':get_asgi_application(), #Handles all normal HTTP requests
      "websocket": AuthMiddlewareStack(# Wraps the URL routing with authentication middleware, so consumers know the user info.
        URLRouter(
            chat.routing.websocket_urlpatterns  # WebSocket routes direct to correct username based on urlpatterns
        )
    ),

}
)
