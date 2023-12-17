from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    #return HttpResponse('Home Page')
    return render(request,"restaurant/home.html")

def menu(request):
     menu_items = Menu.objects.all()
     return render(request, 'restaurant/menu.html', {'menu_items': menu_items})

def tables(request):
    return render(request,"restaurant/tables.html")

def  orders(request):
    return render(request,"restaurant/orders.html")
