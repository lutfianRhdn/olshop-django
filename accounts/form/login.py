from django.forms import ModelForm,ModelChoiceField,FileField,Select,FileInput
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User as UserModel
class LoginFrom(ModelForm):

    class Meta:
        model = UserModel
        fields = ['email', 'password']
        
        labels = {
            'email': _('Email'),
            'password': _('Password'),
        }
        placeholders = {
            'email': _('Email'),
            'password': _('Password'),
        }