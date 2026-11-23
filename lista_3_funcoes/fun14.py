pontuacao = 0

def adicionar_pontos(pontuacao_atual, pontuacaomais):
    return pontuacao_atual + pontuacaomais


def remover_pontos(pontuacao_atual, pontuacaomenos):
    if pontuacao_atual >= pontuacaomenos:
        return pontuacao_atual - pontuacaomenos
    else:
        print("Pontuação não pode ser negativa.")
        return pontuacao_atual


def consultar(pontuacao_atual):
    print(pontuacao_atual)


while True:
    print("==== PONTUAÇÃO ====")
    print('[1] Adicionar Pontos')
    print('[2] Remover Pontos')
    print('[3] Consultar Pontuação')
    print('[4] Sair')

    escolha = int(input("Escolha: "))

    if escolha > 4 or escolha < 1:
        print("Escolha uma opção válida.")
        continue

    if escolha == 4:
        break
    elif escolha == 1:
        pontos = int(input("Digite a quantidade de pontos a serem adicionados: "))
        if pontos > 0:
            pontuacao = adicionar_pontos(pontuacao, pontos)
        else:
            print("Adicione numeros positivos.")
            continue
    elif escolha == 2:
        pts = int(input("Digite a quantidade de pontos a serem removidos: "))
        if pts > 0:
            pontuacao = remover_pontos(pontuacao, pts)
        else:
            print("Digite uma quantidade maior que zero.")
            continue
    elif escolha == 3:
        consultar(pontuacao)