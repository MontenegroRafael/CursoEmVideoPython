#  Programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

nome = str(input('Digite sei nome completo: ')).strip().split()
print('Primeiro nome: {} '.format(nome[0]))
print('Último nome: {} '.format(nome[(len(nome[:])) - 1]))

# print((len(nome[:]) - 1))
