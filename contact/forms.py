from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserContactForm(forms.Form):
    """ Form allowing users to contact site owner with issues/queries"""
    
    name=forms.CharField()
    subject = forms.CharField()
    contact=forms.CharField()
    
    
class UserSalesForm(forms.Form):
    """ Form for users to submit there jersey for resale """
    
    name=forms.CharField()
    jersey = img