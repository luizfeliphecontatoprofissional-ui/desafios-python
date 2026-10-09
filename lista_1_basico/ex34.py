#Conversos de Moedas
reais = float(input("Digite um valor em reais: R$ "))
cot_dol = float(input("Digite a cotação do dólar atual: $ "))
cot_euro = float(input("Digite a cotação do euro atual : € "))

print(f"Seus R$ {reais:.2f} equivalem a: $ {reais / cot_dol:.2f} e € {reais / cot_euro:.2f}")