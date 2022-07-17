#  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário em Python.
#  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
import time
import operator  # para usar itemgetter

jogos = {' Jogador1': random.randint(1, 6),
         ' Jogador2': random.randint(1, 6),
         ' Jogador3': random.randint(1, 6),
         ' Jogador4': random.randint(1, 6)}
ranking = []  # cria uma lista
print('-' * 29)
print(f'{" VALORES SORTEADOS ":=^29}')
for k, v in jogos.items():
    time.sleep(1)
    print(f'{k} tirou ', end='')
    time.sleep(0.5)
    print(f'{v} no dado.')
ranking = sorted(jogos.items(), key=operator.itemgetter(1), reverse=True)
#  abriu uma nova lista para organizar o dicionário 'jogos' pela chave '1'. o 'reverse' usa para ser decrescente
print('=' * 31)
print(f'{" RANKING DOS JOGADORES ":=^31}')
for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar - {v[0]} tirou {v[1]} no dado')
