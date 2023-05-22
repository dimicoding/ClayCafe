from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product
# Create your views here.


def all_products(request):
    """ Renders the view with all off the products available"""

    products = Product.objects.all().order_by('-id')

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Search box empty, type something to search!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'product/product.html', context)


def product_detail(request, product_id):
    """ Renders the view of the specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)
