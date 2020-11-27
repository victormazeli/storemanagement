from django.forms import ModelForm
from marchants.models import Marchant

class LoginForm(ModelForm):

    class Meta:
        model = Marchant
        fields = ['email', 'password']


