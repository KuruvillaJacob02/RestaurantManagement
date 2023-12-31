# Generated by Django 5.0 on 2023-12-17 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_order_items_remove_order_total_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='order',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table'),
        ),
    ]
