#   Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#   na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90,
         'Uniformes', 278)
cont = soma = 0
for l in lista:
    if cont % 2 == 0:
        print(f'{l:.<30} \033[32mR$\033[m', end='')
    if cont % 2 == 1:
        print(f'\033[32m{l:>7.2f}\033[m')
        soma += l
    cont += 1
print('-' * 40)
print('{:.<30} \033[32mR$\033[m'.format('Total'), end='')
print(f'\033[31m{soma:>7.2f}\033[m')
