def maior(a=0, b=0, c=0):
    if a > b and a > c:
        return f"Maior número: {a}"
    elif b > a and b > c:
        return f"Maior número: {b}"
    elif c > a and c > b:
        return f"Maior número: {c}"
    else:
        return "Os números são iguais!"

numeros = []
for i in range(3):
    valor = int(input(f"Digite o {i+1}° número inteiro: "))
    numeros.append(valor)

resultado = maior(numeros[0], numeros[1], numeros[2])
print(resultado)
