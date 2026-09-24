while True:
     print("--- Tabuada ---")
     tabuada = int(input("Qual tabuada? "))
     for i in range(1, 11):
          print(f"{tabuada} X {i} = {tabuada * i}")

     while True:
          sair = input("Deseja parar? [S/N] ").strip().upper()
          if sair in ['S', 'N']:
               break
          print("Opção inválida! Use S para sim e N para não")
     if sair == 'S':
          print("Programa encerrado!")
          break