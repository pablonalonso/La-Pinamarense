session = {}
carro = session.get("shoppingcart")


if not carro:
    print("No hay carro! Lo crearemos a continuacion...")
    carro = session["shoppingcart"] = {}
    print("Se ha creado un carro vacio hasta el momento. ")




carro =  {
        1: {"id_producto": 1,
        "nombre": "Pizza",
        "precio": "500",
        "cantidad": 1,
        "imagen": "pizza.jpg"},

        2: {"id_producto": 2,
        "nombre": "Empanada",
        "precio": "400",
        "cantidad": 1,
        "imagen": "emapanada.jpg"},
        
    }
    



for key, value in carro.items():
    print("ID: {}".format(value["id_producto"]))
    print("Nombre: {}".format(value["nombre"]))
    print("Precio: ${}".format(value["precio"]))
    print("Cantidad: {}".format(value["cantidad"]))
    print("Imagen: {}".format(value["imagen"]))
    print(" ")

