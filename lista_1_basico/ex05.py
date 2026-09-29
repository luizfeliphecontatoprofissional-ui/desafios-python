#soma dos numeros
soma = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    soma += num

print(f"\nA soma total foi {soma}")