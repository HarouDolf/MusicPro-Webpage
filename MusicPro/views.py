from django.shortcuts import render

import random
from django.shortcuts import redirect
from  django.contrib import messages
from .forms import AñadirAlCarroForm
from MusicPro.models import  Productos
from transbank.webpay.webpay_plus.transaction import Transaction

from cart import cart
# Create your views here.
def index(request):
    return render(request, 'index.html')

def producto(request):
    return render(request, 'producto.html')

def mostrarProducto(request):

    cart = cart(request)

    if request.method == 'POST':
        form = AñadirAlCarroForm(request.POST)

        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']

            cart.add(producto_id=Productos.id, cantidad=cantidad, actualizar_cantidad=False)

            messages.success(request, 'Se ah añadido un producto al carro')

            return redirect('producto')
        else:
            form = AñadirAlCarroForm()

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