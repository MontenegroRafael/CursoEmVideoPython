# Programa para refazer o desafio 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triâgulo será formado:

'''
- Equilatero: todos os lados iguis
- Isóceles: dois lados iguis
- Escaleno: todos os lados diferentes
'''

r1 = float(input('\033[33mDigite o primeiro comprimento:\033[m '))
r2 = float(input('\033[32mDigite o segundo  comprimento:\033[m '))
r3 = float(input('\033[31mDigite o terceiro comprimento:\033[m '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('SIM é possivel formar um triângulo com os comprimentos digitados.')
    if r1 == r2 == r3:
        print('E o triâgulo formado será EQUILÁTERO.')
    elif (r1 == r2 or r1 == r3 or r2 == r3) and (r1 != r2 or r1 != r3):
        print('E o triâgulo formado será ISÓSCELES.')
    else:
        print('E o triâgulo formado será ESCALENO.')
else:
    print('NÃO é possivel formar um triângulo com os comprimentos digitados.')
'''
#  Resolução do professor:
# para simplificar o professor da prioridade para fazer as condições mais simples.
#  deichando as mais complexas para o else que naturalmente vai ser a condição que resta. 
#  não precisando escrever nada, já que é a unica opção que falta.
if r1 == r2 == r3:
    print'EQUILÁTERO!'
elif r1 != r2 != r3 != r1:
    print('ESCALENO!')
else:
    print('ISÓSCELES!')
'''
