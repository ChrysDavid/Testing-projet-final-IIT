import json
import pytest
from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer
from chat.models import Salon, Message
from django.contrib.auth.models import User
from school.models import Classe

@pytest.mark.asyncio
@pytest.mark.django_db
async def test_websocket_connect():
    # Création des données nécessaires
    classe = Classe.objects.create(name="Classe Test")
    salon = Salon.objects.create(classe=classe, nom="Salon Test")

    # Configuration du communicateur
    communicator = WebsocketCommunicator(
        ChatConsumer.as_asgi(),
        f"/ws/instructor/messages/{salon.classe.id}/"
    )
    connected, _ = await communicator.connect()
    assert connected

    await communicator.disconnect()

@pytest.mark.asyncio
@pytest.mark.django_db
async def test_fetch_messages():
    # Création des données nécessaires
    user = User.objects.create_user(username="testuser", password="password")
    classe = Classe.objects.create(name="Classe Test")
    salon = Salon.objects.create(classe=classe, nom="Salon Test")
    Message.objects.create(auteur=user, salon=salon, message="Test message")

    communicator = WebsocketCommunicator(
        ChatConsumer.as_asgi(),
        f"/ws/instructor/messages/{salon.classe.id}/"
    )
    await communicator.connect()

    # Envoi d'une commande fetch_messages
    fetch_command = {
        "command": "fetch_messages",
        "classe": salon.classe.id
    }
    await communicator.send_json_to(fetch_command)
    response = await communicator.receive_json_from()

    assert response["command"] == "messages"
    assert len(response["messages"]) == 1
    assert response["messages"][0]["message"] == "Test message"

    await communicator.disconnect()
