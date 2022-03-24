from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=500,blank=True)
