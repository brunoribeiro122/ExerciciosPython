n1 = input('digite o primeiro numero')
n2 = input('digite o segundo numero')
n3 = input('digite o terceiro numero')
if n1 > n2+n3 or n2 > n1+n3 or n3 > n2+n1:
    print('Um dos números é maior que a soma dos outros dois')
else: 
    print('Nenhum dos números é maior que a soma dos outros dois')