#  Programa que leia um número qualquer e mostre o seu fatorial.
#  Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
print('{:-^40}'.format(' Calculadora de Fatorial (!) '))
n = int(input('Digite um número: '))

# opção 1
#import math
#print(' = {}'.format(math.factorial(num)))

# opção 2 - do professor
c = n  # Contador começando com o número digitado.
f = 1  # Como precisamos fazer um multiplicador então começa com '1' pra começar limpo.
       # pois qualquer número multiplicado por 1 vai ser ele mesmo.
print('{}! = '.format(n), end='')  # tem que ficar fora do laço para que não se repita toda vez
while c > 0:
    print('{}'.format(c), end='')  # vai mostrar a sequencia do contador 'c' começando de 5
    if c > 1:  # se 'c' for maior que 1 coloque um ' x '
        print(' x ', end='')
    else:  # se não coloque ' = '
        print(' = ', end='')
    f = f * c  # a multiplicação fica antes do contador por que tem que usar o valor de 'c' antes de subitrair - 1
    c = c - 1  # ex> se 'n = 1' será c=5-1=4 >> c=4-1=3 >> c=3-1=2 >> c=2-1=1  ai sai do laço pois 'c' agora vale 1
print('{}'.format(f))
'''

# opção com 'for'

n = int(input('Digite um número:'))
c = 0
f = 1
print('\033[32m{}!\033[m \033[33m= \033[m'.format(n), end='')
for c in range(n, 0, -1):
    print('\033[3{}m{}\033[m'.format(c, c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c
print('{}'.format(f))



