from django.db import models
from django.contrib.auth.models import User


class extended_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=500,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='static/core/profile')
