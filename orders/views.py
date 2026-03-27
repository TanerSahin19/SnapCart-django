from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from cart.models import CartItem
from .forms import OrderCreateForm
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart:cart_detail")

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user

            total_price = 0
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )
                total_price += item.product.price * item.quantity

            order.total_price = total_price
            order.save()

            cart_items.delete()

            return redirect("orders:success")

    else:
        form = OrderCreateForm()

    context = {
        "form": form,
        "cart_items": cart_items,
    }
    return render(request, "orders/checkout.html", context)

@login_required
def order_success(request):
    return render(request, "orders/success.html")

@login_required
def my_orders(request):
    orders = request.user.orders.all().order_by("-created_at")

    context = {
        "orders": orders,
    }
    return render(request, "orders/my_orders.html", context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    context = {
        "order": order,
    }
    return render(request, "orders/order_detail.html", context)