 # Programa que lê um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math

ângulo = float(input('Digite o valor de um ângulo: '))
# como o float lê o ângulo digitado com graus e a função sen, cos, e tan lê o valor em radianos então precisa converter.
# para isso usa o 'math.radians'

print('O ângulo de {:.2f}° tem como SENO {:.2f}'.format(ângulo, math.sin(math.radians(ângulo))))
print('O ângulo de {:.2f}° tem como COSSENO {:.2f}'.format(ângulo, math.cos(math.radians(ângulo))))
print('O ângulo de {:.2f}° tem como TANGENTE {:.2f}'.format(ângulo, math.tan(math.radians(ângulo))))
'''
# pode siplificar também, importando somente os módulos que vão ser usados.
# ficando assim.

from math import sin, cos, tan, radians

ângulo = float(input('Digite o valor de um ângulo: '))
# como o float lê o ângulo digitado com graus e a função sen, cos, e tan lê o valor em radianos então precisa converter.
# para isso usa o 'math.radians'

print('O ângulo de {:.2f}° tem como SENO {:.2f}'.format(ângulo, sin(radians(ângulo))))
print('O ângulo de {:.2f}° tem como COSSENO {:.2f}'.format(ângulo, cos(radians(ângulo))))
print('O ângulo de {:.2f}° tem como TANGENTE {:.2f}'.format(ângulo, tan(radians(ângulo))))

