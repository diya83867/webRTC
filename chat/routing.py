

from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    re_path('ws/call/', CallConsumer.as_asgi()),
]