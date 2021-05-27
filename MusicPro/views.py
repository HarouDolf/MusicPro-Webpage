from django.shortcuts import render

import random
from django.shortcuts import redirect
from django.contrib import messages
from .forms import AñadirAlCarroForm
from .models import Productos, SUBSUBCATEGORIA_CHOICES, SUBCATEGORIA_CHOICES, CATEGORIA_CHOICES
from transbank.webpay.webpay_plus.transaction import Transaction


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


# WebPay
def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = 'http://transbank-rest-demo.herokuapp.com/webpay_plus/commit'

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
