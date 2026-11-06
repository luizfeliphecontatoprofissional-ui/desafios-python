def ficha(nome, gols=0):
    print(f"Jogador {nome} marcou {gols} gol(s).")

jogador = input("Digite o nome do jogador: ").title().strip()
gol = input("Digite a quantidade de gols (ou Enter para ignorar): ").strip()

if gol == "":
    ficha(jogador)
else:
    ficha(jogador, int(gol))