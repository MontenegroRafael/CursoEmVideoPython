#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado
#  e as suas respectivas posições na lista.

valores = []
for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}° número: ')))
print(f'Você digitou os valores - {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior número digitado foi {maior} e está nas posições', end='')
for i, v in enumerate(valores):  # resolução do professor onde enumera os valores encontrados.
    if v == maior:
        print(f' {i}...', end='')
print(f'\nO menor número digitado foi {menor} e está nas posições', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}...', end='')
