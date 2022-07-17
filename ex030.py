# Programa que lê um número inteiro e mostre na tela se ele é PAR ou Ímpar.

# os números pares quando divididos por 2 deixam resto 0 e os impares deixam resto 1

num = int(input('Digite um número: '))
if (num % 2) == 0:
    print('\033[7;30;43m{} é um número par\033[m'.format(num))
else:
    print('\033[7;30;43m{} é um número Ímpar\033[m'.format(num))
