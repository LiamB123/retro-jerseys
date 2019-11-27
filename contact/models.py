# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class contact(models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    subject= models.CharField(max_length=50, blank=False,null=False)
    message=models.TextField(max_length=300,blank=False,null=False)
    contact= models.EmailField(max_length=80, blank=False,null=False)
    date = models.DateField()
    
    
    
class sales_form(models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    subject= models.CharField(max_length=50, blank=False,null=False)
    message=models.TextField(max_length=300,blank=False,null=False)
    contact= models.EmailField(max_length=80, blank=False,null=False)
    date = models.DateField()
    image = models.ImageField(upload_to="img/received")