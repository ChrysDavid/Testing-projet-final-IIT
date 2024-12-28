from django.urls import resolve
from chat.routing import websocket_urlpatterns

def test_websocket_urlpatterns():
    path = resolve('/ws/instructor/messages/1/')
    assert path.url_name is None  # Pas de nom défini pour cette URL
    assert path.route == r'^ws/instructor/messages/(?P<classe>\w+)/$'
