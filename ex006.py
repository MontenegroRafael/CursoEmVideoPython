# programa que leia um número  e mostre o seu dobro, seu triplo e sua raiz quadrada.

n1 = int(input('Digite um número: '))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)

print('O número digitado foi {:>5} '. format(n1))
print('Seu dobro é {:>5}'.format(n2))
print('Seu triplo é {:>5}'.format(n3))
print('Sua raiz quadrado é {:>5}'.format(n4))
