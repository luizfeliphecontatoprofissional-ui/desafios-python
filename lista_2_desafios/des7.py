#Segundo Maior Número
lista = []

for i in range(6):
    num = int(input("Digite um número: "))
    lista.append(num)

maior = lista[0]
seg = lista[0]

for num in lista[1:]:
    if num > maior:
        seg = maior
        maior = num
    elif num > seg or maior == seg:
        seg = num

print(f"Maior número: {maior}")
print(f"Segundo maior número {seg}")