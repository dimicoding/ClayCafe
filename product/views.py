from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.


def all_products(request):

    """ Renders the view with all off the products available"""

    products = Product.objects.all().order_by('-id')

    context = {
        'products': products,
    }

    return render(request, 'product/product.html', context)


def product_detail(request, product_id):

    """ Renders the view of the specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)
