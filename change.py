def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingrese el gasto: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print("")
    print("Vuelto")
    print("")
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    centavos = round((vuelto - pesos) * 100)
    print(centavos)
