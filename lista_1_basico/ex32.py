#Manipulador de Texto
nome = input("Digite seu nome completo: ").strip()

total_letras = len(nome.replace(" ", ""))
mais = nome.upper()
minus = nome.lower()
letras_primeiro = len(nome.split()[0])

print(f"Nome em maiúsculas: {mais}")
print(f"Nome em minúsculas: {minus}")
print(f"Quantidade de caracteres: {total_letras}")
print(f"Letras no primeiro nome: {letras_primeiro}")