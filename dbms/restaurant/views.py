from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from .forms import OrderForm
from .forms import TableForm
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

def bill(request, pk_test):
    table = Table.objects.get(id=pk_test)
    orders = table.order_set.all()
    total_amount = sum(order.item_price for order in orders)
    context = {'table':table,'orders':orders,'total_amount':total_amount}
    return render(request,"restaurant/bill.html",context)

def  orders(request):
    return render(request,"restaurant/orders.html")

def createOrder(request):
    form = OrderForm
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, "restaurant/order_form.html", context)

def updateOrder(request, pk):
  
    order =  Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, "restaurant/order_form.html", context)

def deleteOrder(request,pk):
    order =  Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context ={'item':order}
    return render(request,'restaurant/delete.html',context)

def updateTable(request, pk):
    table =  Table.objects.get(id=pk)
    form = TableForm(instance=table)
    if request.method == 'POST':
        form = TableForm(request.POST, instance = table)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, "restaurant/table_form.html", context)

def pay(request, pk_test):
    table = Table.objects.get(id=pk_test)
    orders = table.order_set.all()
    total_amount = sum(order.item_price for order in orders)
    if request.method == "POST":
        # Perform payment-related logic if needed

        # Delete all orders associated with the table
        orders.delete()
        transaction = Transaction.objects.create(
            table = table,
            payment_date=timezone.now(), 
            amount=total_amount,
            status = 'Success',
        )
        return redirect('home')  # Redirect to home or another appropriate view after payment and deletion

    context = {'table': table, 'orders': orders}
    return render(request, "restaurant/pay.html", context)

def transactions(request):
     transaction = Transaction.objects.all().order_by('-payment_date')
     return render(request, 'restaurant/transactions.html', {'transaction': transaction})

