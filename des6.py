lista = []

while True:
    num = int(input("Digite um número (ou 0 para parar): "))
    if num == 0:
        break
    lista.append(num)

if len(lista) > 0:
    soma = sum(lista)
    media = soma / len(lista)
    maior = max(lista)
    menor = min(lista)

    print("\n--- Resultado Final ---")
    print(f"Números digitados: {lista}")
    print(f"Quantidade de números armazenados: {len(lista)}")
    print(f"A soma dos números: {soma}")
    print(f"A média total: {media:.2f}")
    print(f"O maior número: {maior}")
    print(f"O menor número: {menor}")
else:
    print("Nenhum valor inserido.")
