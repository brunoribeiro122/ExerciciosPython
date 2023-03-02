print("Vamos calcular seu peso ideal de acordo com sua altura")
sexo = int(input('Digite seu sexo:\n 1- feminino\n 2- Masculino\n  '))
altura = float(input('Digite sua altura:\n '))
if sexo == 1:
    peso = 62.1 * altura - 44.7
    print("Seu peso ideal de acordo com sua altura de", altura,"m e de:", peso )

elif sexo == 2:
    peso = 72.7 * altura - 58
    print("Seu peso ideal de acordo com sua altura de", altura,"m e de:", peso ) 

else: 
    print("Erro digite o sexo novemente")   