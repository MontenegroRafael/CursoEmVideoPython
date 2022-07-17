# Programa que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento

s = float(input('Digite o valor do salário(use ponto no lugar de vírgula) R$ - '))

aum = s * 0.15 #valor do aumento
ns = s + aum #novo salário
print('=' * 80)
print('R$ {:.2f} - Salário atual'.format(s))
print('R$ {:.2f} - aumento(15%)'.format(aum)) # o :.2f ajusta a resposta para apenas 2 casas decimais depois do ponto
print('R$ {:.2f} - Novo valor de salário com aumento de 15%'.format(ns))

