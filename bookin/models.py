from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    userid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class Ticket(models.Model):
    tid=models.IntegerField(primary_key=True,auto_created=True)
    tag=models.CharField(max_length=50)
    start=models.CharField(max_length=50)
    end=models.CharField(max_length=50)
    num=models.IntegerField()
    time=models.TimeField()
    price=models.FloatField()
class Booking(models.Model):
    bid=models.IntegerField(primary_key=True,auto_created=True)
    userid=models.IntegerField()
    tid=models.IntegerField()
    btime=models.TimeField(auto_now=True)
