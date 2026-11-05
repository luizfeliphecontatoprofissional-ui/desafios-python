def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas)/ len(notas)


def situacao(media):
    if media >= 6:
        return f"Média {media:.2f}: Aluno Aprovado!"
    elif media >= 4:
        return f"Média {media:.2f}: Aluno em Recuperação!"
    else:
        return f"Média {media:.2f}: Aluno Reprovado."


def tabela(notas, media, status):
    print("\n" + "=" * 40)
    print(f"{'BOLETIM FINAL':^40}")
    print("=" * 40)

    for i, n in enumerate(notas):
        rotulo = f"Nota {i + 1}"
        print(f"{rotulo:.<35} {n:.2f}")

    print("-" * 40)
    print(f"{'Média Final:':.<35} {media:.2f}")
    print(f"{'Situação:':.<10} {status}")
    print("=" * 40)


qtd = int(input("Quantas notas vai digitar? "))
lista_notas = []

for i in range(qtd):
    nota = float(input(f"Digite a {1+i}° nota: "))
    lista_notas.append(nota)

media_final = calcular_media(lista_notas)
resultado = situacao(media_final)
tabela(lista_notas, media_final, resultado)