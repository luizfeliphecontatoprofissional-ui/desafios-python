#Dia da Semana
'''
dia = int(input("Digite um número (1 a 7): "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sabado")
else:
    print("Número inválido!")
'''
dias = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
dia = int(input("Digite um número (1 a 7): "))

if 1 <= dia <= 7:
    print(dias[dia-1])
else:
    print("Numero inválido!")
