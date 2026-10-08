#Soma dos Dígitos
numero_str = input("Digite um número: ")
soma = 0

for digito in numero_str:
    soma += int(digito)

print(f"A soma dos dígitos é: {soma}")