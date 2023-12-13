from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Home Page')
    return render(request,"restaurant/home.html")

def menu(request):
    return render(request,"restaurant/menu.html")

def tables(request):
    return render(request,"restaurant/tables.html")

def  orders(request):
    return render(request,"restaurant/orders.html")
