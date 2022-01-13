class shopping_cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("shoppingcart")
        if not carro:
            carro = self.session["shoppingcart"] = {}
        self.carro = carro

    
    def agregar(self, producto): 
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]={
                "id_producto": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    break
            self.guardar_carro()

    def guardar_carro(self):
        self.session["shoppingcart"] = self.carro
        self.session.modified=True


    def eliminar(self, producto):
        if str(producto.id) in self.carro.keys():
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["shoppingcart"] = {}
        self.session.modified=True


    



