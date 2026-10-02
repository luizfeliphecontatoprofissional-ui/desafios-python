#Média de Quatro Notas
notas = []
soma = 0
for i in range(4):
    n = float(input(f"Digite a {i + 1}° nota: "))
    soma += n
    notas.append(n)

media = soma / 4

if media > 7:
    print(f"Aprovado!\nMédia final: {media:.2f}")
elif media < 5:
    print(f"Reprovado!\nMédia final: {media:.2f}")
else:
    print(f"Recuperação!\nMédia final: {media:.2f}")