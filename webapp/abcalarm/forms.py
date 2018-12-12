from django import forms
from django.forms import ModelForm
from .models import *


class AlarmForm(ModelForm):

    class Meta:
        model = Alarm
        fields = ['title', 'message', 'status']
