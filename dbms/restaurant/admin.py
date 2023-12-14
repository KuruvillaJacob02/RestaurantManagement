# restaurant/admin.py

from django.contrib import admin
from .models import Table, Menu, OrderItems, Order, Transaction

admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(OrderItems)
admin.site.register(Order)
admin.site.register(Transaction)