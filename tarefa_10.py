
ano  =  2023
anodenascimento  = int(input("Digite o ano de nascimento: "))
idade  =  (ano  -  anodenascimento)

if  idade  >=  16 :
    print ( "Você pode votar este ano. Sua idade é: " , idade )
else :
    print ( "Você não pode votar neste ano. Sua idade é: " , idade, "anos" )