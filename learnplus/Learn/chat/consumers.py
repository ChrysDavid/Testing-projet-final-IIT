from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Salon, Message
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        salon = data['classe']
        messages = Message.objects.filter(salon__classe=int(salon)).order_by('date_add').all()[:20]
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        auteur = data['from']
        salon = data['classe']
        salon_object = Salon.objects.get(classe__id=int(salon))
        auteur_user = User.objects.filter(username=auteur)[0]
        message = Message.objects.create(
            auteur=auteur_user,
            salon=salon_object,
            message=data['message']
        )
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            try:
                result.append(self.message_to_json(message))
            except Exception as e:
                print(f"Erreur lors de la conversion du message: {e}")
                continue
        return result

    def message_to_json(self, message):
        image = None
        try:
            # Essayer d'obtenir l'image de l'étudiant
            if hasattr(message.auteur, 'student_user'):
                image = message.auteur.student_user.photo.url
            # Si ce n'est pas un étudiant, essayer instructeur
            elif hasattr(message.auteur, 'instructor'):
                image = message.auteur.instructor.photo.url
            else:
                # Image par défaut si aucun profil n'est trouvé
                image = '/static/assets/images/default_avatar.png'
        except Exception as e:
            print(f"Erreur lors de la récupération de l'image: {e}")
            image = '/static/assets/images/default_avatar.png'

        return {
            'auteur': message.auteur.username,
            'auteur_image': image,
            'message': message.message,
            'date_add': str(message.date_add.year) + "-" + str(message.date_add.month) + "-" + str(message.date_add.day) + " " + str(message.date_add.hour) + ":" + str(message.date_add.minute) + ":" + str(message.date_add.second)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    def connect(self):
        self.salon = self.scope['url_route']['kwargs']['classe']
        self.room_group_name = 'chat_%s' % self.salon

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))