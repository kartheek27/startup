from django.db import models

# Create your models here.
class Customer(models.Model):
    userid=models.CharField(max_length=6,default='')
    mpin=models.IntegerField(max_length=6,default=000000)
    name=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)
    state=models.CharField(max_length=100,default='')
    district=models.CharField(max_length=100,default='')
    mandal=models.CharField(max_length=100,default='')
    village=models.CharField(max_length=100,default='')
    pin=models.IntegerField(default=0)