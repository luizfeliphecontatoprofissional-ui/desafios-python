#contagem regressiva
from time import sleep

num = int(input("Um número para começar a contagem regressiva! "))
for i in range(num, -1, -1):
    sleep(0.75)
    print(i)