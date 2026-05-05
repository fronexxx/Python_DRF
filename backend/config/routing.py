from django.urls import path

from channels.routing import URLRouter

from apps.chat.routing import websocket_urlpatterns as chat_routing
from apps.pizzas.routing import websocket_urlpatterns as pizza_routin

websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing)),
    path('api/pizzas/', URLRouter(pizza_routin))
]