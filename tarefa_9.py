n = (int(input("Digite o numero de termos: ")))
a1 = (int(input("Digite o valor inicial: ")))
an = (int(input("digite o valor final: ")))
q = (int(input("Digite a razão: ")))
s = (a1 * ( q ** n - 1 ) / ( q - 1 ))

if q >= 2:
    print ("A soma dos termos é:",a1,'*(',q,'**',n,'-1)/(',q,"-1 =")
    print (s)
else: 
    print ("A razão deve ser maior ou igual a 2")