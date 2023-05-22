from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def all_products(request):

    products = Product.objects.all().order_by('-id')

    context = {
        'products': products,
    }

    return render(request, 'product/product.html', context)
