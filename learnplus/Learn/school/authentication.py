from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to find user by username or email
            user = UserModel.objects.filter(
                username=username
            ).first()
            
            if user and user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        return None