#Número Perfeito
num = int(input("Digite um número: "))

divisores = []
soma = 0

for i in range(1, num):
    if num % i == 0:
        divisores.append(i)
        soma += i

divisores_str = ", ".join(map(str, divisores))
print(f"Divisores: {divisores_str}")

soma_str = " + ".join(map(str, divisores))
print(f"{soma_str} = {soma}\n")

if soma == num:
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} NÃO é um número perfeito.")