#Contagem de 1 até N
from time import sleep
N = int(input("Digite um número inteiro positivo: "))

for i in range(1, N+1, 1):
    print(i)
    sleep(0.5)
