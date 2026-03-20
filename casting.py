def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int(input("Ingrese un precio:"))
    descuento = float(input("Ingrese un descuento:"))
    cantidad = int(input("Ingrese la cantidad de precio:"))

    print("Precio:", precio)
    print("Descuento:", descuento)
    precio_descontado = precio - descuento
    print("Precio con descuento:", precio_descontado)
    total = precio_descontado * cantidad
    print("Total:", total)
