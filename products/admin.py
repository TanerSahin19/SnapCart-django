from django.contrib import admin
from .models import Category, Product


# Category modelini admin paneline kaydet
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    # Admin listesinde hangi alanlar görünsün
    list_display = ['name', 'slug', 'created_at']

    # Slug alanını name alanından otomatik doldur
    prepopulated_fields = {'slug': ('name',)}

    # Admin panelde arama yapılabilecek alanlar
    search_fields = ['name']


# Product modelini admin paneline kaydet
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # Admin listesinde görünecek alanlar
    list_display = [
        'name',
        'category',
        'price',
        'stock',
        'available',
        'is_featured',
        'created_at'
    ]

    # Sağ tarafta filtreleme alanları
    list_filter = [
        'available',
        'is_featured',
        'category',
        'created_at'
    ]

    # Arama kutusunda aranabilecek alanlar
    search_fields = ['name', 'description']

    # Slug alanını otomatik name'den doldur
    prepopulated_fields = {'slug': ('name',)}

