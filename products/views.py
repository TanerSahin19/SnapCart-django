from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'home.html', {'products': products})


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/category.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/detail.html', {'product': product})

def search(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        "query": query,
        "results": results,
    }
    return render(request, "products/search.html", context)