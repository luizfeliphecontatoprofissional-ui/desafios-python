#Conversor de Segundos
qtd = int(input("Digite o tempo total em segundos: "))

horas = qtd // 3600
minutos = (qtd % 3600) // 60
seg = qtd % 60

print(f"{qtd} segundos equivalem: {horas}h {minutos}m {seg}s")