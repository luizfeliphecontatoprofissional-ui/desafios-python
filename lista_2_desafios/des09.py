#Lista sem Reptições
original = []
sem_repetição = []

while True:
    num = int(input("Digite um número (ou 0 para parar): "))
    if num == 0:
        break
    original.append(num)

if len(original) > 0:
    for num in original:
        if num not in sem_repetição:
            sem_repetição.append(num)
    print("Original:", original)
    print("Sem repetição:", sem_repetição)
else:
    print("Nenhum valor inserido.")