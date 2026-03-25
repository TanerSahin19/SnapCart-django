from django.shortcuts import get_object_or_404, redirect
from products.models import Product
from .models import CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("products:product_detail", slug=product.slug)