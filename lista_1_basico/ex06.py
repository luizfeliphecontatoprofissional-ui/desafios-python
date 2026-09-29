#maior e menor
numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f"O maior número: {maior}")
print(f"O menor número: {menor}")