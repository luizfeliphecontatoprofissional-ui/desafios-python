"""""""""
Jeito básicão
num1 = input("Digite o 1° número:")
num2 = input("Digite o 2° número:")
num3 = input("Digite o 3° número:")

if num1 > num2 and num1 > num3:
    print("O primero número é o maior")
elif num2 > num1 and num2 > num3:
    print("O segundo número é o o maior")
elif num3 > num1 and num3 > num2:
    print("O terceiro número é o maior")
else:
    print("Os números são iguais.")

if num1 < num2 and num1 < num3:
    print("O primero número é o maior")
elif num2 < num1 and num2 < num3:
    print("O segundo número é o o maior")
elif num3 < num1 and num3 < num2:
    print("O terceiro número é o maior")
"""""""""
numeros = []

for i in range(3):
    num = input(f"Digite o {i+1}° numero: ")
    numeros.append(num)

if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
    print("O primero número é o maior")
elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
    print("O segundo número é o o maior")
elif numeros[2] > numeros[0] and numeros[2] > numeros[1]:
    print("O terceiro número é o maior")
else:
    print("Os números são iguais.")

if numeros[0] < numeros[1] and numeros[0] < numeros[2]:
    print("O primero número é o menor")
elif numeros[1] < numeros[0] and numeros[1] < numeros[2]:
    print("O segundo número é o o menor")
elif numeros[2] < numeros[0] and numeros[2] < numeros[1]:
    print("O terceiro númeor é o menor")
