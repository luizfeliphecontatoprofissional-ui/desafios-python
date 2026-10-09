#Contador de Vogais
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input("Digite sua palavra: ")).lower()
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print(f"Vogais: {contador}")

