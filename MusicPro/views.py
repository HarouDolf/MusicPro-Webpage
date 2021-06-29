import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Productos, SUBSUBCATEGORIA_CHOICES, SUBCATEGORIA_CHOICES, CATEGORIA_CHOICES, Categoria, \
    Subcategoriacuerdas
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .forms import RegUsr, LoginForm
from django.db.models import Q
from MusicPro.cart import Cart
from MusicPro.context_processor import cart_total_amount


# Create your views here.
def index(request):
    cart = Cart(request)
    productos = Productos.objects.all()
    categorias = Categoria.objects.all()
    subcategoriacuerdas = Subcategoriacuerdas.objects.all()
    args = {'productos': productos, 'categorias': categorias, 'Subcategoriacuerdas': Subcategoriacuerdas,
            'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'index.html', args)


def producto(request):
    cart = Cart(request)
    productos = Productos.objects.all()
    args = {'productos': productos, 'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'producto.html', args)


def busqueda(request, categoria):
    cart = Cart(request)
    productos = Productos.objects.all().filter(categoria_producto__contains=categoria)
    args = {'productos': productos, 'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'busqueda.html', args)


def detalle(request, producto_id):
    cart = Cart(request)
    productos = get_object_or_404(Productos, pk=producto_id)
    args = {'productos': productos, 'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'detalle.html', args)


def login1(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(username=data.get("usr"), password=data.get("passwd"))
        if user is not None:
            login(request, user)
            messages.success(request, 'Ha iniciado sesion correctamente!')
            return redirect("/")
        else:
            messages.warning(request, 'Usuario y/o contraseña incorrectos!')
    return render(request, "login.html", {"form": form})

def logout(request):
    django_logout(request)
    return redirect("/")

def registro(request):
    form = RegUsr
    if request.method == "POST":
        form = RegUsr(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado con exito!')
            return redirect("/login")
    else:
        form = RegUsr()
    return render(request, "registro.html", {"form": form})

#cart

@csrf_protect
def add_product_catalogo(request, productos_id):
    cart = Cart(request)
    product = Productos.objects.get(id=productos_id)
    cart.add(product=product)
    return redirect("/producto/")


def add_product_carrito(request, productos_id):
    cart = Cart(request)
    product = Productos.objects.get(id=productos_id)
    cart.add(product=product)
    return redirect("/cart/")



@csrf_protect
def remove_product(request, productos_id):
    cart = Cart(request)
    product = Productos.objects.get(id=productos_id)
    cart.remove(product)
    return redirect("/cart/")


@csrf_protect
def decrement_product(request, productos_id):
    cart = Cart(request)
    product = Productos.objects.get(id=productos_id)
    cart.decrement(product=product)
    return redirect("/cart/")


@csrf_protect
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/cart/")

# WebPay
def webpay_plus_create(request):
    total = 0
    FprecioC = 0
    cart = Cart(request)
    buy_order = str(1)
    session_id = str(1)
    return_url = 'http://127.0.0.1:8000/webpay_plus/commit'
    total = 0
    FprecioC = 0

    for key, value in request.session['cart'].items():
        total = total + (float(value['price']) * value['quantity'])
        # FprecioC=(f'{total:.3f}')
        FprecioC= int(total)
    amount = FprecioC
    try:
        response = Transaction().create(buy_order, session_id, amount, return_url)
        print(amount)
        return render(request, 'cart.html', {"response":response})
    except TransbankError as e:
        print(e.message)
        return render(request, 'cart.html', {})


def webpay_plus_commit(request):
    token = request.POST.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = Transaction.commit(token=token)
    print("response: {}".format(response))

    data = {
        'token': token,
        'response': response
    }
    return render(request, 'Webpay/commit.html', data)
