print("0 - FIM\n1 - INCLUI\n2 - ALTERA\n3 - EXCLUI\n4 - CONSULTA")
opcao = (int(input("Selecione uma opção: ")))
if opcao == 0:
    print("FIM")
if opcao == 1:
    print("INCLUI")
if opcao == 2:
    print("ALTERA")
if opcao == 3:
    print("EXCLUI")
if opcao == 4:
    print("CONSULTA")
if opcao > 4:
    print("ERRO....")
    print("Valor diferente do menu. Item não encontrado")