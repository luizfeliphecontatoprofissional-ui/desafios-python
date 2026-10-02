#Acima da média de Números
numeros = []
acimamedia = []
soma = 0
for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)

media = sum(numeros) / 5

for n in numeros:
    if n > media:
        acimamedia.append(n)


print(f"Média: {media:.2f}")
print(f"Números acima da média: {acimamedia}")
