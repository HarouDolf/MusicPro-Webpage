from django import template
register = template.Library()
from .models import Productos


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def añadir(self, productos):
        if str(productos.id) not in self.cart.keys():
            self.cart[productos.id] = {
                "product_id": productos.id,
                "name": productos.nombre,
                "quantity": 1,
                "price": str(productos.precio),
                "image": productos.image,

            }
        else:
            for key, value in self.cart.items():
                if key == str(productos.id):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.guardar()

    def guardar(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def eliminar(self, productos):
        product_id = str(productos.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.guardar()

    def quitarProducto(self, productos):
        for key, value in self.cart.items():
            if key == str(productos.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.eliminar(productos)
                else:
                    self.guardar()
                break
            else:
                print("El producto no existe en el carrito")

    def limpiar(self):
        self.session["cart"] = {}
        self.session.modified = True