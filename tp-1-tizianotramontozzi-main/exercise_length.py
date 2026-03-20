def length():
    """
    Ejercicio 7 - Conversión de Unidades de Longitud

    Dada una distancia en metros, convertir e imprimir:
    1. Kilómetros (1 km = 1000 m)
    2. Millas (1 milla ≈ 1609.34 m)
    3. Pies (1 pie ≈ 0.3048 m)
    4. Pulgadas (1 pulgada ≈ 0.0254 m)
    """
    metros = 1000

    kílometros = metros / 1000
    millas = metros / 1609.34
    pies = metros / 0.3048
    pulgadas = metros / 0.0254

    print(kílometros)
    print(millas)
    print(pies)
    print(pulgadas)

length()