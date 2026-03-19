from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    balance = models.IntegerField(default=1000)

