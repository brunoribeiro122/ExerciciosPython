#"Escreva um programa que o 
#usuário deva entrar com o nome do aluno e sua nota.
#aluno e sua nota. Exiba o valor
#conforme abaixo
igual = (str("========="))
nome = (input("Digite o nome do aluno"))
nota = (input("Nota do aluno"))

print (" Aluno(a)        NOTA\n","=========     =========\n",nome,"          ",nota)

#resolução usando os placeholders na string

print("{:<12}   {:<6.1f}".format(nome, nota))
print("{:<12}   {:<6.1f}".format(igual, igual))