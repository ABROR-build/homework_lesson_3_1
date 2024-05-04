from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/<int:pk>/', views.show_products, name='show_products'),
    path('product/<int:pk>/', views.show_product, name='show_product')

]
