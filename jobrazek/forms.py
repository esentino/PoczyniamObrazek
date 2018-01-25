from django.forms import Form, ModelForm
from .models import Jobrazek
class ObrazkowyForm(ModelForm):
    class Meta:
        model = Jobrazek
        fields = ['obrazkowa_sciezka']
