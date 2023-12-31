"""
URL configuration for dbms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurant import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name ="home"),
    path('tables/<str:pk_test>/',views.tables, name = "tables"),
    path('menu/', views.menu, name = "menu"),
    path('orders/', views.orders),
    path('create_order/', views.createOrder, name= "create_order"),
    path('update_order/<str:pk>', views.updateOrder, name= "update_order"),
    #path('update_order/<str:pk>', views.updateOrder, name= "update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name= "delete_order"),
    path('update_table/<str:pk>', views.updateTable, name= "update_table"),
    path('bill/<str:pk_test>/',views.bill, name = "bill"),
    path('pay/<str:pk_test>/',views.pay, name = "pay"),
    path('transactions/', views.transactions, name = "transactions"),

]
