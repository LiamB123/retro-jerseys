# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse 
from .forms import UserContactForm, SalesForm
from .models import contact, sales_form
from django.contrib.auth.decorators import login_required

# Create your views here.

def contact_form(request):
    """ returns the contact form"""
    
    if request.method == 'POST':
            form = UserContactForm(request.POST)
            if form.is_valid():
                return HttpResponse('Thanks for contacting us!')
    else:
            form = UserContactForm
    
    return render(request, 'contact.html', {'form': form})


@login_required
def sales_form(request):
    """ a view that returns a submission form for a user to sell a product"""
    
    if request.method == 'POST':
            form = SalesForm(request.POST)
            if form.is_valid():
                return HttpResponse('Thanks for contacting us!')
            
    else:
            
            form = SalesForm
    
    return render(request, 'sales_form.html',{'form': form})
    