from django.shortcuts import render
from .models import Product


def home(request):
    # Sadece satışta olan ürünleri çek
    # En yeni eklenen ürünler üstte gelsin
    products = Product.objects.filter(available=True)

    # Home template'ine products verisini gönder
    context = {
        'products': products,
    }

    return render(request, 'home.html', context)