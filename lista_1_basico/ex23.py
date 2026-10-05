#Custo de Viagem

distancia = float(input("Digite a distância da viagem(quilômetros): "))
consumo = float(input("Digite o consumo do carro (km/l): "))
preco = float(input("Digite o preço do litro do combustível: "))

litros = distancia / consumo

print(f"Serão necessários: {litros:.2f} litros")
print(f"O custo da viagem: R$ {litros * preco:.2f}")