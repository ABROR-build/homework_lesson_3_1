from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_sale, name='list_sale'),
    path('rent/<int:pk>/', views.list_rent_houses, name='list_rent_houses'),
    path('sale/<int:pk>/', views.list_sales_houses, name='list_sales_houses'),

]
