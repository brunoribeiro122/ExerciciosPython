poligono = int(input("Digite o número de lados do poligono: "))
if poligono < 3:
    print('Não é um poligono')
elif poligono == 3:
    print("O poligono é um Triangulo")
    base = float(input('Digite o tamanho da base do triangulo'))
    altura = float(input('Digite a altura do triangulo'))
    print ('a área do triangulo é: ',base*altura/2)
elif poligono == 4:
    print('O poligono é um Quadrado')
    lado1 = float(input('Digite o tamanho de um lado do quadrado'))
    print (lado1**2)
elif poligono == 5:
    print ('O poligono é um Pentagono')
elif poligono > 5:
    print('Poligono nao identificado')
