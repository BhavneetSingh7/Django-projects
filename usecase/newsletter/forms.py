from django.forms import ModelForm
from . models import *

class CredsForm(ModelForm):

    class Meta :
        model = Creds
        fields = '__all__'