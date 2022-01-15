from django import forms
from django.db.models import fields
from django.forms.fields import CharField
from django.forms.widgets import SelectDateWidget
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserFrom(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')

    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        labels=('password1','Password','password2','Confirm Password')


class ProfileForm(forms.ModelForm):
    image=forms.FileField()
    class Meta:
        model=Register
        fields=('phone','image','user_type')



class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')

class UpdateProfileForm(forms.ModelForm):
    address=forms.Textarea()
    
    class Meta:
        model=Register
        fields=('phone','image',)


class EventForm(forms.ModelForm):
    description=forms.Textarea()
    event_date=forms.DateField(label='Event Date',widget=SelectDateWidget)
    
    class Meta:
        model=Event
        fields=('event_name','event_date','event_area','event_time','description')



class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('complaint',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('title','feedback')