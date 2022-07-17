#  Programa que lê o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('\033[33mDigite o primeiro comprimento:\033[m '))
r2 = float(input('\033[32mDigite o segundo  comprimento:\033[m '))
r3 = float(input('\033[31mDigite o terceiro comprimento:\033[m '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('SIM é possivel formar um triângulo com os comprimentos digitados.')
else:
    print('NÃO é possivel formar um triângulo com os comprimentos digitados.')
