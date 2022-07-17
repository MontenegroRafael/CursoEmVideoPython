# Programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))
n0 = n1 - 1
n2 = n1 + 1
print('O antecessor do numero digitado é {}'.format(n0))
print('O sucessor do número digtado é {}'.format(n2))
print('{}, {:|^4}, {} '.format(n0, n1, n2))
