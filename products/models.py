from django.db import models
from django.urls import reverse
from django.utils.text import slugify
class Category(models.Model):
    # Kategori adı
    name = models.CharField(max_length=120, unique=True)

    # Otomatik üretilecek slug alanı
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    # Oluşturulma tarihi
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Kategorileri alfabetik sırala
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        # Admin panelde kategori adını göster
        return self.name

    def save(self, *args, **kwargs):
        # Slug boşsa name alanından otomatik oluştur
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Kategori detay/list sayfası için URL döndür
        return reverse('products:category_products', args=[self.slug])


class Product(models.Model):
    # Ürün hangi kategoriye bağlı
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    # Ürün adı
    name = models.CharField(max_length=200)

    # Ürün slug alanı
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    # Ürün açıklaması
    description = models.TextField(blank=True)

    # Ürün fiyatı
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Ürün görseli
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Stok
    stock = models.PositiveIntegerField(default=0)

    # Satışta mı?
    available = models.BooleanField(default=True)

    # Öne çıkan ürün mü?
    is_featured = models.BooleanField(default=False)

    # Oluşturulma tarihi
    created_at = models.DateTimeField(auto_now_add=True)

    # Güncellenme tarihi
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Yeni ürünler üstte gelsin
        ordering = ['-created_at']

    def __str__(self):
        # Admin panelde ürün adını göster
        return self.name

    def save(self, *args, **kwargs):
        # Slug boşsa name alanından otomatik oluştur
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Ürün detay sayfası için URL döndür
        return reverse('products:product_detail', args=[self.slug])