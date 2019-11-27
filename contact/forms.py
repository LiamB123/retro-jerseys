from django import forms
from .models import contact,sales_form

class UserContactForm(forms.ModelForm):
    """ Form allowing users to contact site owner with issues/queries"""
    class Meta:
        model=contact
        fields=('name','subject','message','contact')
        
   
    
    
class SalesForm(forms.Form):
    """ Form for users to submit there jersey for resale """
    class Meta:
        model=sales_form
        fields=('name','subject', 'message', 'contact','image')