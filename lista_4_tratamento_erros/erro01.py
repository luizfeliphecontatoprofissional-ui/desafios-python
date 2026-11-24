def conversor():
    """
    Converte uma temperatura de Celsius para Fahrenheit.
    :return: Temperatura digitada em Celsius e a temperatura convertida para Fahrenheit.
    """
    while True:
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            return celsius, fahrenheit
        except ValueError:
            print("Erro! Digite uma temperatura válida.")


celsius, fahrenheit = conversor()
print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")
