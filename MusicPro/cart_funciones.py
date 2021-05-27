def cart_total_amount(request):
    total = 0
    Tprecio = 0

    for key, value in request.session['cart'].items():
        total = total + (float(value['price']) * value['quantity'])
        # Tprecio=(f'{total:.3f}')
        Tprecio = int(total)
    return {'cart_total_amount': Tprecio}
