"""
URL configuration for SnapCart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from orders import views

urlpatterns = [
    # Admin panel yolu
    path('admin/', admin.site.urls),

    # Ana sayfa (BOŞ PATH)
    # "" demek: site açıldığında direkt buraya gelir
    # Bu path products app içindeki urls.py'ye yönlendirir
    path('', include('products.urls')),

    # Sepet sistemi
    path('cart/', include('cart.urls')),

    # Sipariş sistemi
    path('orders/', include('orders.urls')),


    # Kullanıcı sistemi (login/register)
    path('accounts/', include('accounts.urls')),
    
]

# MEDIA dosyaları (resimler) için
# Development ortamında yüklediğin resimlerin görünmesini sağlar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
