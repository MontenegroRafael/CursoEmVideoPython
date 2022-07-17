# Programa que lê o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''
import datetime

ano = int(input('Digite seu ano de nascimento: '))
hoje = 2017 #datetime.date.today().year
idade = hoje - ano

if idade <= 9:
    print('Você tem {} anos e sua Categoria é a {}.'.format(idade, 'MIRIN'))
elif 9 < idade <= 14:
    print('Você tem {} anos e sua Categoria é a {}.'.format(idade, 'INFANFIL'))
elif 14 < idade <= 19:
    print('Você tem {} anos e sua Categoria é a {}.'.format(idade, 'JUNIOR'))
elif 19 < idade <= 25:
    print('Você tem {} anos e sua Categoria é a {}.'.format(idade, 'SÊNIOR'))
else:
    print('Você tem {} anos e sua Categoria é a {}.'.format(idade, 'MASTER'))

# resolução do professor:

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
# como já passou pela condição anterior então não precisa repetir a condição. é disnecessario colocar 9 < idade
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
