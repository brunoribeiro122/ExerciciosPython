
idade  =  int ( input ( "Digite sua idade: " ))
categoria  =  input ( "Digite sua categoria (estudante, aposentado, etc.):" )
dia_semana  =  input ( "Digite o dia da semana (segunda, terça, quarta, quinta ou sexta.): " )
if  idade  >=  60 :
    n1  =  '30%'
    print('Você tem direito a', n1,'de desconto')
elif  categoria  ==  "estudante"  and ( dia_semana  ==  "segunda"  or  dia_semana  ==  "terça" ):
    n1  =  '20%'
    print('Você tem direito a', n1,'de desconto')
elif  categoria  ==  "aposentado" :
    n1  =  '15%'
    print('Você tem direito a', n1,'de desconto')
elif  categoria  ==  "aniversariante" :
    n1  =  '50%'
    print('Parabens você tem direito a', n1,'de desconto')
else:
    print ( "Você não tem direito a nenhum desconto." )

