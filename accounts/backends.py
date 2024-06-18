
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate( email=None, password=None):
        UserModel = get_user_model()
        try:
        
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            print('User not found')
            return "User not found"
            return None
        else:
            if user.check_password(password):
                return user
