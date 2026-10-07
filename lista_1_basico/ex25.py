#Compra parcelada
print("PARCELAS! se fizer por mais que 3x tem um juros de 10%")
preco = float(input("Digite o preço do produto: R$ "))
qtd = int(input("Digite a quantidade de parcelas totais: "))


if qtd <= 1:
    print(f"Você vai pagar à vista o valor de: R$ {preco:.2f}")
elif qtd <= 3:
    print(f"Você vai pagar {qtd}x parcelados um valor de {preco / qtd:.2f}")
else:
    print(f"Você vai pagar em {qtd} vezes com 10% de juros: R$ {(preco * 1.10)/ qtd:.2f}")