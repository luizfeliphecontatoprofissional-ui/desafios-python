#Palíndromo
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não é um palíndromo!")
