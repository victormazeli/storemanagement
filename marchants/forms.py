from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Marchant

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Marchant
        fields = ['email', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Marchant
        fields = ['email']