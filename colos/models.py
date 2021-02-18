from django.db import models

# Create your models here.


class UserModel(models.Model):
    highScore = models.CharField(max_length=500)
    userName = models.CharField(max_length=100)