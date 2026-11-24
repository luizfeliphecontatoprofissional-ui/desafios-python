def conversor(celsius):
    """
    Converte uma temperatura de Celsius para Fahrenheit.
    :param celsius: Temperatura em graus Celsius.
    :return: Temperatura convertida para Fahrenheit.
    """
    return (celsius * 9/5) + 32


help(conversor)
print(conversor(30))

def dobro(numero):
    """
    Recebe um número e retorna o dobro dele.
    :param numero: Número recebido.
    :return: Retorna o dobro do número recebido.
    """
    return numero * 2


help(dobro)
print(dobro(10))

def calcular_area(largura, altura):
    """
    Calcula a área de um retângulo.
    :param largura: Largura do retângulo.
    :param altura: Altura do retângulo.
    :return: Área calculada(largura * altura).
    """
    area = largura * altura
    return area


help(calcular_area)
print(f'{calcular_area(8, 4):.2f}')
