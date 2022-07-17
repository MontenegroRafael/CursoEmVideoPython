#  Crie um programa que leia o nome e o preço de vários produtos.
#  O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-=' * 20)
print('Cadastro de Produtos')
print('-=' * 20)
cont = total = cont1000 = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o preço do Produto R$: '))
    cont += 1
    op = str(input('Deseja cadastras mais um produto? [S/N]: ')).strip().upper()[0]
    while op not in 'S,N':
        op = str(input('Opção invalida. Deseja cadastras mais um produto? [S/N]: ')).strip().upper()[0]
    total += preço
    if preço > 1000:
        cont1000 += 1
    if cont == 1:
        menor = preço
        nomebara = nome
    if preço < menor:
        menor = preço
        nomebara = nome
# resolução do professor
# pode simplificar os dois blocos anteriores pois as execuções são iguais.
# ficando assim:
# if cont == 1 or preço < menor:
#   menor = preço
#   nomebara = nome

    if op == 'N':
        break
print('-' * 30)
print('Resumo dos cadastros')
print('-' * 30)
print(f'{cont} produto(s) cadastrados.')
print(f'{total:.2f} real(is) é o total dos valores cadastrados')
print(f'{cont1000} produto(s) custa(m) mais de R$1000,00 reais')
print(f'{nomebara} de R${menor:.2f} é o produto mais barato cadastrado.')
