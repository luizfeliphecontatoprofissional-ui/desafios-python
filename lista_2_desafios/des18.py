#Ranking de Pontuações
ranking = []
from time import sleep
while True:
    nome = input("Nome do jogador: ").strip().title()
    pontuacao = int(input("Pontuação: "))

    jogador = {"nome": nome, "pontuacao": pontuacao}
    ranking.append(jogador)

    continuar = input("Quer continuar a adicoinar jogadores? [S/N]: ").upper()
    if continuar not in ["S", "N"]:
        print("Resposta inválida! Digite S ou N.\n")
        continue
    elif continuar == "N":
        break

ranking_ordenado = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)

print("\n=== RANKING DE JOGADORES ===")
for posicao, jogador in enumerate(ranking_ordenado, start=1):
    sleep(0.3)
    print(f"{posicao}º {jogador['nome']} — {jogador['pontuacao']} pontos")
