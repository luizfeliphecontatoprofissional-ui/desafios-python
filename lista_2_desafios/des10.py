#Separador de Números
par = []
impar = []
neg = []

for i in range(10):
    num = int(input(f"Digite o {i+1}° número: "))

    if num % 2  == 0:
        par.append(num)
    else:
        impar.append(num)

    if num < 0:
        neg.append(num)

print("Números pares:", par)
print("Números impares:", impar)
print("Números negativos:", neg)