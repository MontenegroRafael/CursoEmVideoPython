#  Programa que lê três números e mostre quem é o maior e qual é o menor.

n1 = float(input('\033[33mDigite o primeiro número: \033[m'))
n2 = float(input('\033[34mDigite o segundo número: \033[m'))
n3 = float(input('\033[31mDigite o terceiro número: \033[m'))

if n1 > n2 and n1 > n3:
    print('O maior número digitado foi \033[1;33m{}\033[m'.format(n1))
if n2 > n3 and n2 > n1:
    print('O maior número digitado foi \033[1;34m{}\033[m'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número digitado foi \033[1;31m{}\033[m'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor número digitado foi \033[1;33m{}\033[m'.format(n1))
if n2 < n3 and n2 < n1:
    print('O menor número digitado foi \033[1;34m{}\033[m'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número digitado foi \033[1;31m{}\033[m'.format(n3))

# a resolução do professor

# para verificar quem é o menor

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))

# para verificar quem é o maior

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))
