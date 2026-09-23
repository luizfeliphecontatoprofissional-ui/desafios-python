num = int(input("Digite um número: "))

if num > 0:
    print("O numero é positivo!", end=' ')
elif num == 0:
    print("O numero é zero!", end=' ')
else:
    print("O numero é negativo!", end=' ')

if num % 2 == 0:
    print("e par!")
else:
    print("e impar!")