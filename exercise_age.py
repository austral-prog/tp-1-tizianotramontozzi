def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25

    edad_meses = edad_anos * 12
    edad_días = edad_anos * 365
    edad_horas = edad_días * 24
    edad_minutos = edad_horas * 60

    print(edad_meses)
    print(edad_días)
    print(edad_horas)
    print(edad_minutos)

age()


