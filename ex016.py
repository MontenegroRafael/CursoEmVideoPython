# Programa que lê um número real qualquer pelo teclado e mostre a sua parte inteira.
'''
import math

num = float(input('Digite um número: '))
print('O número escolhido foi {} e sua parte inteira é {}'.format(num, math.floor(num)))

# resolução pelo professor

from math import trunc # para importar somente o modulo 'trunc'
# import math  # pode tambem importar a biblioteca toda 'math'

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))  
# caso seja importada a biblioteca toda então usa - se  'math.trunc'

'''
 # Outra solução também é sem precisar importar modulos

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a parte inteira dele é {}'.format(num, int(num))) # esta função int é de inteiro
