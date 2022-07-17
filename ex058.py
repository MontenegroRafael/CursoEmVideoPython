#   Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#   Só que agora o jogador vai tentar adivinhar até acertar,
#   mostrando no final quantos palpites foram necessários para vencer.

import random
import time

tent = 1

print('Vou pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar?')
time.sleep(2)
comp = random.randint(0, 10)
jogador = int(input('Digite o seu Palpite: '))
if jogador == comp:
    print('Parabéns! Você jogou {} e o computador {} também.'.format(jogador, comp))
    print('ACERTOU DE PRIMEIRA!')
else:
    while jogador != comp:
        if jogador > comp:
            print('ERROUU! É menos.')
            jogador = int(input('Digite um novo Palpite: '))
        elif jogador < comp:
            print('ERROUU! É mais.')
            jogador = int(input('Digite um novo Palpite: '))
        else:
            jogador == comp
            print('Parabéns! Você jogou {} e o computador {} também.'.format(jogador, comp))
        tent = tent + 1
print('Você usou {} tentativas para acertar'.format(tent))


#  resolução do professor

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10,')
print('Será que você consegue adivinhar qual foi? ')
acertou = False  # variável começa com False
palpites = 0
while not acertou:  # enquanto não acertou execute. no caso enquanto 'acertou' for False
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

