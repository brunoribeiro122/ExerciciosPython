n1 = float(input('Insira a primeira nota'))
n2 = float(input('Insira a segunda nota'))
notas = (n1+n2)
if notas > 60 and n1 >= 40 and n2 >= 40:
    print('O aluno passou')
else: 
    print('Aluno REPROVADO')