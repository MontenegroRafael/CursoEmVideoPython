# Programa que faça o computador jogar jokenpô com você.
# pedra papel e tesoura

import random
import time

'''
computador = random.randrange(1, 4)
if computador == 1:
    pc = 'Papel'
elif computador == 2:
    pc = 'Pedra'
else:
    pc = 'Tesoura'

print('Vamos jogar? PEDRA, PAPEL OU TESOURA?')
vc = str(input('Escreva sua escolha: ')).strip().upper()
print('-' * 40)
print('Pedra !')
time.sleep(1)
print('Papel!')
time.sleep(1)
print('Tesoura!')
time.sleep(1)
print('-' * 40)
if (vc == 'PEDRA' and pc == 'Tesoura') or (vc == 'PAPEL' and pc == 'Pedra') or (vc == 'TESOURA' and pc == 'Papel'):
    print('Você VENCEU! \nO computador colocou {} e você {}'.format(pc, vc.title()))
elif (pc == 'Pedra' and vc == 'TESOURA') or (pc == 'Papel' and vc == 'PEDRA') or (pc == 'Tesoura' and vc == 'PAPEL'):
    print('Você PERDEU! \nO computador colocou {} e você {}'.format(pc, vc.title()))
else:
    print('Empatou! O computador colocou {} e vc {}'.format(pc, vc.title()))
'''

# resolução do professor

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)  # vai ficar sorteando entre 0, 1 e 2
# print('O computador escolheu {}'.format(itens[computador]))
# vai pegar dentro de 'itens' a posição que sair no sorteio de computador.
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[31mJO\033[m')
time.sleep(1)
print('\033[33mKEN\033[m')
time.sleep(1)
print('\033[34mPO!!!\033[m')
print('-' * 40)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-' * 40)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # computador jogou PAPEL
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
