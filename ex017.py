# programa que lê o comprimento de cateto oposto e do cateto adjacente de um triângulo,
# calcule e mostre o comprimento da hipotenusa.
'''
import math
co = float(input('Digite o comprimento do cateto OPOSTO: '))
ca = float(input('Digite o comprimento do cateto ADJACENTE: '))


print('=' * 40)
print('{} comprimento do cateto oposto'.format(co))
print('{} comprimento do cateto adjacente'.format(ca))
print('{:.2f} comprimento da hipotenusa'.format(math.hypot(ca, co)))
'''
# outra solução esta do professor

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = ((co ** 2) + (ca ** 2)) ** (1/2)

print('Hipotenusa vai medir {:.2f}'.format(hi))
