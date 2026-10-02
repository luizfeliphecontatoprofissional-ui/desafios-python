#Soma de 1 até N

N = int(input("Digite um número: "))

soma = 0
for i in range(1, N+1):
    soma += i
    if i < N:
        print(f"{i} + ", end='')
    else:
        print(f"{i} = {soma}")
