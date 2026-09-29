#Média do aluno
notas = []

for i in range(3):
    num = float(input(f"Digite a {i+1}° nota: "))
    notas.append(num)

media = sum(notas) / len(notas)

print(f"\nMédia Final: {media:.2f}")

if media >= 7:
    print("Aprovado!")
elif media < 5:
    print("Reprovado")
else:
    print("Recuperação")