# Faça um Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# mostra um emoji de fogos estourando.

import time
import emoji
print('=-' * 20)
print('{:=^40}'.format(' CONTAGEM REGRESSIVA '))
print('=-' * 20)

for cont in range(10, -1, -1):
    time.sleep(1)
    print(cont)
print('BOOMMM!')

print(emoji.emojize(':fireworks:' * 40))
print(emoji.emojize(':sparkles:' * 40))
print(emoji.emojize(':sparkler:' * 40))
