#Frequência de um Número
numeros = []
contador = 0

for i in range(8):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)

procurado = int(input("Digite o número procurado: "))

for num in numeros:
    if procurado == num:
        contador += 1

print(f"O número {procurado} aparece {contador} vezes.")
