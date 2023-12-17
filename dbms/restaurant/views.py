from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    tables = Table.objects.all()
    total_orders = orders.count()
    served = orders.filter(status ='Served').count()
    pending = orders.filter(status = 'Preparing').count()
    context = {'orders':orders, 'tables':tables,'total_orders':total_orders,'pending':pending,'served':served}
    return render(request,"restaurant/home.html", context)

def menu(request):
     menu_items = Menu.objects.all()
     return render(request, 'restaurant/menu.html', {'menu_items': menu_items})

def tables(request, pk_test):
    table = Table.objects.get(id=pk_test)
    orders = table.order_set.all()
    order_count = orders.count()
    context = {'table':table,'orders':orders,'order_count':order_count}
    return render(request,"restaurant/tables.html",context)

def  orders(request):
    return render(request,"restaurant/orders.html")
