# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200, default='')
    description= models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='media/img')
    team=models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name