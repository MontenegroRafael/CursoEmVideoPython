#  Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#  No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite mais um número: '))
v4 = int(input('Digite o último número: '))
valores = (v1, v2, v3, v4)
# resolução do professor
'''
valores = (int(input('Digite um número: ')), 
            int(input('Digite outro número: ')), 
            int(input('Digite mais um número: ')), 
            int(input('Digite o último número: ')))
'''
print(valores)
print(f'O número 9 apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'O número 3 foi digitado a primeira vez na {valores.index(3) + 1}° posição.')
else:
    print('O número 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram ', end='')
for v in valores:
    if v % 2 == 0:
        print(f'| {v} ', end='')


