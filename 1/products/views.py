from django.shortcuts import render
from . import models


def homepage(request):
    categories = models.Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'homepage.html', context=context)


def show_products(request, pk):
    products = models.Products.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)


def show_product(request, pk):
    product = models.Products.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)

