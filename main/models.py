from django.db import models
from django.utils import timezone
from datetime import date
import uuid

TYPE_CHOICES = (
                ('I','investor'),
                ('F','farmer'),
                )

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=11,blank=True)
    DOB = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250)
    bauth = models.CharField(max_length=12 ,blank=True )
    adnum = models.CharField(max_length=10, blank=True  )
    password = models.CharField(max_length=8, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields

def __str__(self):
        return self.fname
# class Type(models.Model):
    
#     type = models.ForeignKey(['M','f'])

# class plan(models.Model):
#     amount = models.DecimalField(max_digits=10)
#     silver = amount*5
#     stdate = models.DateField(timezone.now())
class Login(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=200)
    description = models.CharField(max_length=200)

def __unicode__(self):
    return self.name