from django import forms
from django.forms.fields import CharField
from django.forms.widgets import SelectDateWidget
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ComposeMailForm(forms.ModelForm):
    class Meta:
        model=Mail
        fields=('receiver','subject','message','image','key')