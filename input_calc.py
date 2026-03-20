def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = int(input("Ingrese el numero base: "))
    altura = int(input("Ingrese el numero altura: "))
    area = base * altura
    perimetro = 2 * base + 2 * altura

    print("Base:", base)
    print("Altura:", altura)
    print("Area:", area)
    print("Perimetro:", perimetro)
