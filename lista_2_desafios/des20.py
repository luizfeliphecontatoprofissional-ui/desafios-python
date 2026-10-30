#Números Perfeitos em um Intervalo
def perfeito(n):
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n

inicio = int(input("Início: "))
fim = int(input("Fim: "))

print(f"\nNúmeros perfeitos entre {inicio} e {fim}:")
encontrou = False

for num in range(inicio, fim + 1):
    if perfeito(num):
        print(num)
        encontrou = True

if not encontrou:
    print(f"Não existe nem um número perfeito entre {inicio} e {fim}.")