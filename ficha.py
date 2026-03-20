def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    nombre_completo = (input("Ingrese un nombre completo: ").rstrip()).lstrip()
    email = input("Ingrese un email: ")
    tres_notas = [str(input("Ingrese la 1era nota: ")), str(input("Ingrese la 2da nota: ")),
                  str(input("Ingrese la 3ra nota: "))]

    encabezado_decorativo = """========================
    FICHA DEL ALUMNO
========================"""

    print(encabezado_decorativo)
    print("Nombre:", nombre_completo.title())
    print("Email:", email.lower())
    print("Caracteres en nombre:", len(nombre_completo))
    # Cambiamos las comillas del espacio " " por comillas simples ' '
    print("Iniciales:", f"{nombre_completo[0].upper()}{nombre_completo[nombre_completo.find(' ') + 1].upper()}")
    print("Usuario:", f'{(nombre_completo[nombre_completo.find(" ") + 1:]).lower()}.{(nombre_completo[0:nombre_completo.find(" ")]).lower()}')
    print("Email valido:", "@" in email)
    print("Dominio:", email.lower()[email.find("@") + 1:])
    print("Nombre para archivo:", nombre_completo.replace(" ", "_").title())
    print("Cantidad de a:", (nombre_completo.lower()).count("a"))
    print("Codigo secreto:", nombre_completo[::-1].upper())
    print("Nota 1:", tres_notas[0])
    print("Nota 2:", tres_notas[1])
    print("Nota 3:", tres_notas[2])
    print("Suma:", int(tres_notas[0]) + int(tres_notas[1]) + int(tres_notas[2]))
    print("Promedio:", (int(tres_notas[0]) + int(tres_notas[1]) + int(tres_notas[2])) / 3)
    print("Promedio entero:", int((int(tres_notas[0]) + int(tres_notas[1]) + int(tres_notas[2])) / 3))
    print("=" * 24)

