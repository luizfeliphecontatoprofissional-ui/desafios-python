def analisar(*numeros):
    soma = sum(numeros)
    if len(numeros) == 0:
        return "Nenhum numero informado!"
    else:
        media = soma / len(numeros)
        return f'Quantidade de numeros: {len(numeros)}\nMaior: {max(numeros)}\nMenor: {min(numeros)}\nSoma: {soma}\nMédia: {media:.2f}'


lista = []
qtd = int(input("quantos números quer somar? "))
for i in range(qtd):
    num = int(input(f"Digite {i+1}° número inteiro: "))
    lista.append(num)

print(analisar(*lista))