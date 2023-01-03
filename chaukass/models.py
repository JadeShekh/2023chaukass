from django.db import models

class Sat(models.Model):
    imei= models.CharField(max_length=100)
    msg= models.CharField(max_length=100)
    lat= models.CharField(max_length=200)
    long= models.CharField(max_length=200)
    samay=models.CharField(max_length=200)