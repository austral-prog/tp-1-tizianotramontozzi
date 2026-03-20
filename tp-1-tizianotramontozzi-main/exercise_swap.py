def swap():
    """
    Ejercicio 9 - Intercambio de Variables

    Dados dos valores x e y, intercambiar sus valores e imprimir:
    1. El valor original de x
    2. El valor original de y
    3. El valor de x después del intercambio
    4. El valor de y después del intercambio
    """
    x = 10
    y = 20

    print(x)
    print(y)

    x, y = y, x

    print(x)
    print(y)

swap()