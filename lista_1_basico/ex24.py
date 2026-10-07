#Salário com Comissão 5 %

sal = float(input("Digite um salário fixo: R$ "))
val_tot = float(input("Valor total das vendas: R$ "))

print(f"O salário final é: R$ {sal + (val_tot * 0.05):.2f}")