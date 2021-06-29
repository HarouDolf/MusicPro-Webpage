"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from MusicPro import views
from django.conf import settings
from MusicPro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('producto/', views.producto, name='producto'),
    path('detalle/<int:producto_id>',views.detalle, name='detalle'),
    path('login/',views.login1, name='login'),
    path('registro/',views.registro, name='registro'),
    path('busqueda/<str:categoria>',views.busqueda, name='busqueda'),
    path('webpay_plus/commit', views.webpay_plus_commit, name='webpay_commit' ),
    path('add_product_catalogo/<int:productos_id>/', add_product_catalogo, name='add_product_catalogo'),
    path('add_product_carrito/<int:productos_id>/', add_product_carrito, name='add_product_carrito'),
    path('cart/', views.webpay_plus_create, name='cart'),
    path('remove_product/<int:productos_id>/', remove_product, name='remove_product'),
    path('decrement_product/<int:productos_id>/', decrement_product, name='decrement_product'),
    path('clear/', clear_cart, name='clear_cart'),
    path('logout/',logout,name='logout')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

