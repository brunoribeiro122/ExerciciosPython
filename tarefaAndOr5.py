alfabetizada = str(input('Você sabe ler e escrever ? s/n'))
idade = int(input('Digite sua idade'))
if alfabetizada == 's' and idade >= 25:
    print('Sim, a pessoa é alfabetizada e tem mais de 25 anos')
elif alfabetizada == 'n' and idade >= 25:
    print('A pessoa não é alfabetizada e tem mais de 25 anos')
elif alfabetizada == 's' and idade <= 25:
    print('A pessoa é alfabetizada e tem menos de 25 anos')
elif alfabetizada == 'n' and idade <= 25:
    print('A pessoa não é alfabetizada e tem menos de 25 anos')
else:
    print('Não, a pessoa não é alfabetizada e tem menos de 25 anos')