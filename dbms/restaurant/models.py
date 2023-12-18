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

class Order(models.Model):
    STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Served', 'Served'),
    ]
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    item_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        # Automatically set item_price based on the selected meal
        if not self.item_price and self.meal:
            self.item_price = self.meal.meal_price * self.quantity
        super(Order, self).save(*args, **kwargs)
    def __str__(self):
        return f"Order {self.pk} - Table {self.table.pk}"


'''class Order(models.Model):
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
        return f"Order {self.pk} for Table {self.table.pk}"'''



class Transaction(models.Model):
    STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
        ('Refund', 'Refund'),
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    payment_date = models.DateTimeField(auto_now_add=True, null =True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
