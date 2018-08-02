from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    accessKey = models.CharField(max_length=50)
    secretKey = models.CharField(max_length=50)
    def __str(self)__:
        return selt.username

