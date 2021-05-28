import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Productos, SUBSUBCATEGORIA_CHOICES, SUBCATEGORIA_CHOICES, CATEGORIA_CHOICES
from transbank.webpay.webpay_plus.transaction import Transaction
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from .forms import RegUsr, LoginForm
from.cart import Cart


# Create your views here.
def index(request):
    productos = Productos.objects.all()
    args = {'productos': productos, 'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'index.html', args)


def producto(request):
    productos = Productos.objects.all()
    args = {'productos': productos, 'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'producto.html', args)

def detalle(request, producto_id):
    productos = get_object_or_404(Productos, pk=producto_id)
    args = {'productos': productos, 'CATEGORIA_CHOICES': CATEGORIA_CHOICES,
            'SUBCATEGORIA_CHOICES': SUBCATEGORIA_CHOICES, 'SUBSUBCATEGORIA_CHOICES': SUBSUBCATEGORIA_CHOICES}
    return render(request, 'detalle.html', args)

def login1(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user = authenticate(username=data.get("usr"), password=data.get("passwd"))
        if user is not None:
            login(request,user)
            messages.success(request,'Ha iniciado sesion correctamente!')
            return redirect("/")
        else:
            messages.warning(request,'Usuario y/o contraseña incorrectos!')
    return render(request,"login.html", {"form":form})

def registro(request):
    form = RegUsr
    if request.method == "POST":
        form = RegUsr(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Se ha registrado con exito!')
            return redirect("/login")
    else:
        form = RegUsr()
    return render(request, "registro.html", {"form":form})


def cart(request):
    return render(request, 'cart.html')


def add_product_carrito(request, productos_id):
    cart = Cart(request)
    productos = producto.objects.get(id=productos_id)
    cart.añadir(productos=productos)
    return redirect("/cart.html")


@csrf_protect
def decrement_product(request, instrument_id):
    cart = Cart(request)
    instrument = producto.objects.get(id=instrument_id)
    cart.quitarProducto(instrument=instrument)
    return redirect("/cart.html")

@csrf_protect
def remove_product(request, instrument_id):
    cart = Cart(request)
    instrument = producto.objects.get(id=instrument_id)
    cart.eliminar(instrument)
    return redirect("/cart.html")

@csrf_protect
def clear_cart(request):
    cart = Cart(request)
    cart.limpiar()
    return redirect("/cart.html")



# WebPay
def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = 1955000
    return_url = 'http://127.0.0.1:8000/webpay_plus/commit'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = Transaction.create(buy_order, session_id, amount, return_url)

    data = {
        'response': response
    }
    print(response)

    return render(request, 'Webpay/create.html', data)


def webpay_plus_commit(request):
    token = request.POST.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = Transaction.commit(token=token)
    print("response: {}".format(response))

    data = {
        'token' : token,
        'response' : response
    }
    return render(request, 'Webpay/commit.html', data)

