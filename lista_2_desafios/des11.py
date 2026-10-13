#Analisador de Palavras
palavras = []

while True:
    palavra = input("Digite uma palavra (ou FIM para encerrar): ").strip()

    if palavra.upper() == "FIM":
        break

    if palavra:
        palavras.append(palavra)
    else:
        print("Você não digitou nenhuma palavra válida. Tente novamente.")

if len(palavras) > 0:
    mais_longa = palavras[0]
    mais_curta = palavras[0]
    total_caracteres = 0

    for p in palavras:
        total_caracteres += len(p)

        if len(p) > len(mais_longa):
            mais_longa = p

        if len(p) < len(mais_curta):
            mais_curta = p

    print(f"\n=== RESULTADOS ===")
    print(f"Quantidade de palavras: {len(palavras)}")
    print(f"Palavra mais longa: {mais_longa}")
    print(f"Palavra mais curta: {mais_curta}")
    print(f"Quantidade total de caracteres: {total_caracteres}")
else:
    print("Nenhuma palavra foi digitada.")