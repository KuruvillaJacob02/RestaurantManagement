from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Home Page')
    return render(request,"restaurant/home.html")

def menu(request):
    return HttpResponse('Menu')

def  orders(request):
    return HttpResponse('Orders')
