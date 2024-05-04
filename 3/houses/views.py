from django.shortcuts import render
from .models import *


def list_sale(request):
    sales_types = SalesTypes.objects.all()
    context = {
        'sales_types': sales_types
    }
    return render(request, 'list_sales.html', context)


def list_rent_houses(request, pk):
    rent_houses = ForRent.objects.filter(type=pk)
    context = {
        'rent_houses': rent_houses
    }
    return render(request, 'list_rent_houses.html', context=context)


def list_sales_houses(request, pk):
    sales_houses = ForSale.objects.filter(type=pk)
    context = {
        'sales_houses': sales_houses
    }
    return render(request, 'list_sales_houses.html', context=context)
