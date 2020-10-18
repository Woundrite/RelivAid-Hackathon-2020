from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

#Create your models here

class LabourModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    currentLocation = models.CharField(max_length=200)
    gotoLocation = models.CharField(max_length=200)
    aadharNumber = models.CharField(max_length=14)

    def __str__(self):
        r = (self.name)
        return r

class PickerModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    preferToStayAnonymous = models.BooleanField()
    ishelper = models.BooleanField(default=0)
    aadharNumber = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class MedicalPill(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.name