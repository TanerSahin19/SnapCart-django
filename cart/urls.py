from django.urls import path 
from . import views


app_name = "cart"


urlpatterns = [
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("increase/<int:item_id>/", views.increase_cart_item, name="increase_cart_item"),
    path("decrease/<int:item_id>/", views.decrease_cart_item, name="decrease_cart_item"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("", views.cart_detail, name="cart_detail"),
]