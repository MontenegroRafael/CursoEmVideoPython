#  Crie um programa onde o usuário possa digitar sete valores numéricos e
#  cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))

    if n % 2 == 0:
        valores[0].append(n)  # tem que indereçar em 'valores'
    else:
        valores[1].append(n)
print(f'Os valores digitados foram - {valores}')
print(f'{sorted(valores[0])} São Pares.')
print(f'{sorted(valores[1])} São Ímpares.')

