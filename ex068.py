#  Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder,
#  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import random

cont = 0
print('-' * 40)
print('Vamos Jogar PAR ou ÍMPAR ?')
print('-' * 40)
while True:
    v = int(input('Digite um valor: '))
    op = str(input('PAR ou ÍMPAR [P/I]')).upper().strip()
    while op not in 'P,I':
        op = str(input('Opção invalida. PAR ou ÍMPAR [P/I]: ')).strip().upper()[0] # pra pegar só a primeira letra só
    comp = random.randint(0, 10)
    total = v + comp
    if (op == 'P' and total % 2 == 0) or (op == 'I' and total % 2 == 1):
        print('-' * 40)
        print('Você VENCEU!')
        print('-' * 40)
        cont += 1
        if op == 'P' and total % 2 == 0:
            print(f'Você jogou {v} e o computador {comp}. Total de {total}. DEU PAR')
        if op == 'I' and total % 2 == 1:
            print(f'Você jogou {v} e o computador {comp}. Total de {total}. DEU ÍMPAR')
        print('Vamos jogar novamente? ')
    else:
        print('-' * 40)
        print('Você PERDEU!')
        print('-' * 40)
        if op == 'I' and total % 2 == 0:
            print(f'Você jogou {v} e o computador {comp}. Total de {total}. DEU PAR')
        if op == 'P' and total % 2 == 1:
            print(f'Você jogou {v} e o computador {comp}. Total de {total}. DEU ÍMPAR')
        break
print('-' * 40)
print(f'GAME OVER!, Você venceu {cont} vezes.')
'''
#  resolução do professor

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '  # começa vaziu
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]  # [0] pega somente a primeira letra
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')  # operador ternário. tudo em uma linha só
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente?... ')
print(f'GAME OVER! Você venceu {v} vezes.')
