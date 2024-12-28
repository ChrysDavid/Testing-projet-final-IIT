import pytest
from django.contrib.auth.models import User
from chat.models import Salon, Message
from school.models import Classe

@pytest.mark.django_db
def test_create_salon():
    classe = Classe.objects.create(name="Classe Test")
    salon = Salon.objects.create(classe=classe, nom="Salon Test")
    assert salon.nom == "Salon Test"
    assert salon.classe == classe

@pytest.mark.django_db
def test_message_creation():
    user = User.objects.create_user(username="testuser", password="password")
    classe = Classe.objects.create(name="Classe Test")
    salon = Salon.objects.create(classe=classe, nom="Salon Test")
    message = Message.objects.create(auteur=user, salon=salon, message="Test message")
    assert message.auteur == user
    assert message.salon == salon
    assert message.message == "Test message"
