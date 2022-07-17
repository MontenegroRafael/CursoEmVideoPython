#  Faça um programa que mostre a tabuada de vários números, um de cada vez,
#  para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo.

import time
while True:
    n = int(input('Digite um número para ver sua Tabuada: '))
    if n >= 0:
        for c in range(1, 11):
            print(f'{n} * {c} = ',end='')
            time.sleep(0.5)
            print(f'{n * c}')
            time.sleep(0.5)
    else:
        break
print('Finalizado!')
