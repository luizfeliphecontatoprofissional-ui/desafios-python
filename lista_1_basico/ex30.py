#Divisível por 3 e 5
num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("Numero divisível por 3 e 5!")
elif num % 5 == 0:
    print("Numero divisível por 5!")
elif num % 3 == 0:
    print("Numero divisível por 3!")
else:
    print("Não é divisível por nenhum dos números.")