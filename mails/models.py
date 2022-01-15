from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from account.models import *
from django.core.validators import RegexValidator


# Create your models here.


class Mail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    receiver=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    image=models.FileField(upload_to='images',null=True,blank=True)
    key=models.CharField(max_length=50,validators=[RegexValidator(regex='^.{6}$', message='Length has to be 6', code='nomatch')])
    trash=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)
