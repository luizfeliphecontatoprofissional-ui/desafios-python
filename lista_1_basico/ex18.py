#Contagem de Múltiplos de 3

ini = int(input("Valor inicial: "))
fim = int(input("Valor final: "))

multiplos = []
for i in range(ini, fim+1):
    if i % 3 == 0:
        multiplos.append(i)

print(f"Múltiplos de 3 encontrados: {multiplos}")
print(f"Total de múltiplos: {len(multiplos)}")