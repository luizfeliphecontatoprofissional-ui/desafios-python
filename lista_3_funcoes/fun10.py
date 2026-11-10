def somar(*numeros):
    print(numeros)
    return sum(numeros)


lista = []
qtd = int(input("quantos números quer somar? "))
for i in range(qtd):
    num = int(input(f"Digite {i+1}° número inteiro: "))
    lista.append(num)

print('\nA soma:')
print(somar(*lista))