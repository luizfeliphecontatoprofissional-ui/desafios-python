#Quantidade de Dígitos
num = abs(int(input("Digite um número: ")))

if num < 10:
    print("1 dígito")
elif num < 100:
    print("2 dígitos")
elif num < 1000:
    print("3 dígitos")
else:
    print("4 ou mais dígitos")
