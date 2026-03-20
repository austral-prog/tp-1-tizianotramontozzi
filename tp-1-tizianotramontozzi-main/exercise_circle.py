from math import pi


def circle():
    """
    Ejercicio 6 - Geometría de Círculo

    Dado el radio de un círculo, calcular e imprimir:
    1. El área (π × radio²)
    2. La circunferencia (2 × π × radio)
    """
    radio = 5

    area = pi * radio**2
    circunferencia = 2 * pi * radio

    print(area)
    print(circunferencia)

circle()
