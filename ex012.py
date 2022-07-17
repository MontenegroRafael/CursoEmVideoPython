# Programa que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.

p = float(input('Digite o preço(use ponto no lugar da vírgula) R$ - '))

d = p * 0.05 # a resolução do prfessor utilizou regra de três. tipo . pc = p - (p * 5/100)
pc = p - d

print('=' * 80)
print('R$ {:.2f} - Valor sem desconto.'.format(p)) # pra dinheiro sepre use a formatação :.2f
print('R$ {:.2f} - de desconto(5%).'.format(d))
print('' * 1)
print('R$ {:.2f} - Valor total com desconto de 5%'.format(pc))
