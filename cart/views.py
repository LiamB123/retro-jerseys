# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, redirect, reverse 


def view_cart(request):
    """
    a view that renders the cart contents page
    """
    return render(request,'cart.html')
    
def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart 
    """
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart',{})
    cart[id]=cart.get(id, quantity)
    
    request.session['cart']=cart
    return redirect(reverse('index'))
    
def adjust_cart(request, id):
    """
    Adjust the quantity of a specified producrt to the specified amount 
    """
    
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart',{})
    
    if quantity > 0:
        cart[id]=quantity
    else:
        cart.pop(id)
        
    request.session['cart']=cart
    return redirect(reverse('view_cart'))