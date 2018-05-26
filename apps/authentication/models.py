from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20,unique=True,primary_key=True)
    bio = models.CharField(max_length=50)
    image = models.URLField()
    token = models.CharField(max_length=500)
