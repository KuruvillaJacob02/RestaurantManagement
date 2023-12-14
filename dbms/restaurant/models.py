# restaurant/models.py

from django.db import models

class Table(models.Model):
    STATUS_CHOICES = [
        ('Vacant', 'Vacant'),
        ('Occupied', 'Occupied'),
        ('Reserved', 'Reserved'),
    ]
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    #order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Table {self.pk}: {self.status}"

class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Beverage', 'Beverage'),
    ]

    meal_name = models.CharField(max_length=255)
    meal_price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    def __str__(self):
        return f"{self.meal_name} - {self.category}"

class OrderItems(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Item {self.pk} in Order {self.order.pk}: {self.meal.meal_name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Served', 'Served'),
    ]

    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    items = models.ManyToManyField(OrderItems, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def __str__(self):
        return f"Order {self.pk} for Table {self.table.pk}"




class Transaction(models.Model):
    STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
        ('Refund', 'Refund'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
