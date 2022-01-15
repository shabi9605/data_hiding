from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.

class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField()
    image=models.FileField(upload_to='images',null=True,blank=True)
    manager='manager'
    programmer='programmer'
    user_types=[
        (manager,'manager'),
        (programmer,'programmer')
    ]
    user_type=models.CharField(max_length=50,choices=user_types,default=programmer)
    
    def __str__(self):
        return str(self.user.username)



class Event(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    event_name=models.CharField(max_length=50)
    event_date=models.DateField()
    event_area=models.CharField(max_length=50)
    event_time=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.event_name)



class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.TextField()
    def __str__(self):
        return str(self.user.username)



class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50)
    feedback=models.TextField()
    def __str__(self):
        return str(self.user.username)
