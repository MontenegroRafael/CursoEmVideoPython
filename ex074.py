#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e
#  também indique o menor e o maior valor que estão na tupla.

from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
sorteados = (n1, n2, n3, n4, n5)

print(f'Os valores sorteados foram: {n1} {n2} {n3} {n4} {n5}')
maior = n1
menor = n1
for n in sorteados:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if n == n5:
        break
print(f'O maior número sorteado é {maior}.')
print(f'O menor número sorteado é {menor}.')

# resoloção do professor

números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10),)
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')  # 'max' traz o maoir dentro da Tupla
print(f'O menor valor sorteado foi {min(números)}')  # 'min' traz o menor dentro da Tupla

