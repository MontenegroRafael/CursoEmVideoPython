# Programa que faça p computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print('-=-' * 20)
print('\033[7;30;43mDescubra o número que o computador pensou.\033[m')
print('-=-' * 20)
num = int(input('Digite um número entre 0 e 5: '))
print('P R O C E S S A N D O . . . . . . . ')
time.sleep(3)
numpc = random.randint(0, 5)
if num == numpc:
    print('Você \033[1;32;40mACERTOU!\033[m O computador pensou em {} e você em {} também'.format(numpc, num))
else:
    print('\033[1;31m:P ERROU !!!\033[m')
    print('O computador pensou em {}'.format(numpc))
