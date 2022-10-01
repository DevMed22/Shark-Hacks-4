from django.db import models
from django.contrib.auth.models import User



class Player(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    survive = models.PositiveSmallIntegerField(default=0)
    death = models.PositiveSmallIntegerField(default=0)