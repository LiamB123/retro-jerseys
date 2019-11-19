# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Product 

# Create your tests here.

def ProductTests(TestCase):
    
    def test_str(self):
        test_name = Product(name="{{product.name}}")