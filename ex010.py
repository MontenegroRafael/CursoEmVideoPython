# Programa que leia quanto uma pessoa tem na carteira e mostre quantos dollares ela pode compra.
# considerar US$ 1,00 = R$ 3,27

r = float(input('Digite o valor em Reais(use ponto no lugar da vírgula) R$ - '))
cd = float(input('Digite qual é a cotação do dolar no momento em Reais(use ponto no lugar da vírgula) R$ - '))

d = r / cd

print('=' * 80)
print('R$ {:.2f} da pra comprar: '.format(r))
print('US$ {:.2f} dolares'.format(d))
