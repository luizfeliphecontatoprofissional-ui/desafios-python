def calcular_preco(preco, desconto=0):
    valor_desconto = preco * (desconto / 100)
    return preco - valor_desconto


valor = float(input("Digite o valor do produto: R$"))
percentual = float(input("Digite a procentagem do desconto: "))

preco_final = calcular_preco(valor, percentual)

print(f"Preço original: R${valor}")
print(f"Porcentagem: {percentual}%")
print(f"Valor final: R${preco_final:.2f}")
