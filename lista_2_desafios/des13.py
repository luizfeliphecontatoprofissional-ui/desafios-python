#Contador de Letras

palavra = input("Digite uma palavra: ").strip().lower().replace(" ", "")

contador = {}

for letra in palavra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(f"A palavra foi {palavra}:")
for letra, quantidade in contador.items():
    print(f'{letra} = {quantidade}')