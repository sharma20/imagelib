from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.user_id


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    caption = models.CharField(max_length=50, default="")
