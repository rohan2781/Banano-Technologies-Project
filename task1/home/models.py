from django.db import models
from django.contrib.auth.models import User


class extended_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=500,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='static/core/profile')
    type = models.BooleanField(default=True)

class Blog(models.Model):
    user= models.CharField(max_length=80,default='NULL')
    title = models.CharField(max_length=80,default='NULL')
    image=models.ImageField(null=True,blank=True,upload_to='static/core/profile')
    category = models.CharField(max_length=80,default='NULL')
    summary=models.TextField(max_length=500,blank=True)
    content=models.TextField(max_length=500,blank=True)
    draft= models.BooleanField(default=False)

