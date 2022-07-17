# Programa que lê os nomes de quatro alunos e sorteie um.

import random

a1 = str(input('Digite o primeiro nome: '))
a2 = str(input('Digite o segundo nome: '))
a3 = str(input('Digite o terceiro nome: '))
a4 = str(input('Digite o quarto nome: '))

lista = [a1, a2, a3, a4] # tem que criar uma lista para que a função execute. Uma lista fica sempre entre [] cochetes.

print('O nome escolhido foi -->> {}'.format(random.choice(lista)))  # o módulo 'choice' escolha em inglês.
