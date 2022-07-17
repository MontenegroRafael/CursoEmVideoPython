# Programa que lê o nome de quatro alunos e mostre a ordem sorteada.
import random

a1 = str(input('Digite o 1° nome: '))
a2 = str(input('Digite o 2° nome: '))
a3 = str(input('Digite o 3° nome: '))
a4 = str(input('Digite o 4° nome: '))

lista = [a1, a2, a3, a4] # cria a lista
random.shuffle(lista) # Embaralha a lista

print('A ordem sorteada foi --->> {}'.format(lista)) # mostra a lista já embaralhada


