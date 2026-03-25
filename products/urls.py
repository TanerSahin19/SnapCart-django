from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("category/<slug:slug>/", views.category_products, name="category_products"),
    path("<slug:slug>/", views.product_detail, name="product_detail"),
]