from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    tel = models.IntegerField()
    email = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.username
