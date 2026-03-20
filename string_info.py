def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    longitud = len(palabra)

    print(f'Palabra: {palabra}')
    print(f'Longitud: {longitud}')
    print(f'Primera letra: {palabra[0]}')
    print(f'Ultima letra: {palabra[-1]}')
    print(f'Repetida: {palabra * 3}')
    print (f'Decorada: ***{palabra}***')
