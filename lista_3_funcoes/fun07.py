def formatar_nome(nome, sobrenome):
    return f"{nome} {sobrenome}"


primeiro_nome = input("Digite seu primeiro nome: ").strip().title()
sobre_nome = input("Digite seu sobrenome: ").strip().title()

nome_completo = formatar_nome(primeiro_nome, sobre_nome)

print(f"Nome completo: {nome_completo}")