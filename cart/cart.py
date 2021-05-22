from django.conf import settings

from MusicPro.models import Productos

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

        def __iter__(self):
            for p in self.cart.keys():
                self.cart[str(p)]['productos'] = Productos.objects.get(pk=p)

                for item in self.cart.values():
                    item['precio_total'] = item['productos'].precio * item['cantidad']

                    yield item

        def __len__(self):
            return sum(item['cantidad'] for item in self.cart.values())

        def add(self, producto_id, cantidad=1, actualizar_cantidad=False):
            producto_id = str(producto_id)

            if producto_id not in self.cart:
                self.cart[producto_id] = {'cantidad': 1, 'id': producto_id}

            if actualizar_cantidad:
                self.cart[producto_id]['cantidad'] += int(cantidad)

                if self.cart[producto_id]['cantidad'] == 0:
                    self.remove(producto_id)

                self.save()

        def remove(self, producto_id):
            if producto_id in self.cart:
                del self.cart[producto_id]
                self.save()


        def save(self):
            self.session[settings.CART_SESSION_ID] = self.cart
            self.session.modified = True

        def clear(self):
            del self.session[settings.CART_SESSION_ID]
            self.session.modified = True

        def get_costo_total(self):
            for p in self.cart.keys():
                    self.cart[str(p)]['producto'] = Productos.objects.get(pk=p)

            return sum(item['cantidad'] * item['producto'].precio for item in self.cart.values())



