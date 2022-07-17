#  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#  entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from time import sleep
from random import randint

temp = []
jogos = []
nj = int(input('Quantos jogos quer fazer? '))
print(f'Sorteando {nj} Jogos')
for c in range(0, nj):
    for j in range(0, 6):
        n = randint(1, 60)
        while n in temp:
            n = randint(1, 60)
        temp.append(n)
    temp.sort()
    jogos.append(temp[:])
    temp.clear()

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
print('Boa Sorte!')

