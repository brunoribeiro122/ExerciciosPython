idade = int(input('Digite a sua idade'))
autori = str(input('Você tem autorização S/N'))
if idade >= 18 or autori == 'S':
    print ('acesso liberado')
else: 
    print('Acesso negado')