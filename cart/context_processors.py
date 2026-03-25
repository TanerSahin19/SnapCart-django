from .models import CartItem

def cart_item_count(request):
    count = CartItem.objects.count()
    return {"cart_item_count": count}