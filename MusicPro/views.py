from django.shortcuts import render

import random
from django.shortcuts import redirect
from  django.contrib import messages
from .forms import AñadirAlCarroForm
from MusicPro.models import  Productos
from transbank.webpay.webpay_plus.transaction import Transaction
from django.views.decorators.csrf import csrf_protect
from.cart import Cart

from cart import cart
# Create your views here.
def index(request):
    return render(request, 'index.html')

def producto(request):
    return render(request, 'producto.html')


def add_product_carrito(request, instrument_id):
    cart = Cart(request)
    instrument = producto.objects.get(id=instrument_id)
    cart.añadir(instrument=instrument)
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
    amount = random.randrange(10000, 1000000)
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