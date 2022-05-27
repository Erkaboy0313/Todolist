from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    list_name = models.ForeignKey(UserList,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    is_done = models.BooleanField()

    def __str__(self):
        return self.name