def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12

    promedio = (num1 + num2 + num3 + num4) / 4
    máximo = max(num1, num2, num3, num4)
    mínimo = min(num1, num2, num3, num4)
    rango = máximo - mínimo

    print(promedio)
    print(máximo)
    print(mínimo)
    print(rango)

statistics()
