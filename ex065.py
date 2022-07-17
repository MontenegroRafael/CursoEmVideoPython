#  Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = soma = maior = menor = 0

opção = 'S'
while opção == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    opção = str(input('Quer continuar? [S/N]:')).strip().upper()
    while opção not in 'SN':
        opção = str(input('Opção invalida.Quer continuar? [S/N]: ')).strip().upper()
print('Você digitou {} números e a média foi {}'.format(cont, soma/cont))
print('O maior foi {} e o menor foi {}.'.format(maior, menor))
