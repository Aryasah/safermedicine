from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=122,blank=True,null=True)
    email = models.CharField(max_length=122,blank=True,null=True)
    phone = models.CharField(max_length=12,blank=True,null=True)
    desc = models.TextField(default="none",blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    uname = models.CharField(max_length=122,blank=True,null=True)
    month = models.IntegerField(max_length=4,blank=True,null=True)
    year = models.IntegerField(max_length=4,blank=True,null=True)
    cardNumber = models.IntegerField(default="none",blank=True,null=True)
    cvv = models.IntegerField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    fname = models.CharField(max_length=122,blank=True,null=True)
    lname = models.CharField(max_length=122,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    file= models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=122,blank=True,null=True)
    phone = models.CharField(max_length=12,blank=True,null=True)
    desc = models.TextField(default="none",blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


