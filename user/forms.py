'''
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from .utils import ActivationMailFormMixin

class UserCreationForm(ActivationMailFormMixin, UserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

    mail_validation_error = 'User created. Could not send activation email. Please try again later.'
    
    def save(self, **kwargs):
        
'''
