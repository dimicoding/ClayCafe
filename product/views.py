from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product
from urllib.parse import unquote
# Create your views here.


def all_products(request):
    """ Renders the view with all off the products available"""

    products = Product.objects.all().order_by('-id')
    query = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # python documentation for urllib.parse and unquote https://docs.python.org/3/library/urllib.parse.html
        if 'category' in request.GET:
            encoded_categories = request.GET.getlist('category')
            categories = [unquote(category) for category in encoded_categories]
            products = products.filter(category__cat_name__in=categories)
            categories = Category.objects.filter(cat_name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Search box empty, type something to search!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'product/products.html', context)


def product_detail(request, product_id):
    """ Renders the view of the specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)

