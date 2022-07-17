#   Aprimore o desafio anterior, mostrando no final:
#   A) A soma de todos os valores pares digitados.
#   B) A soma dos valores da terceira coluna.
#   C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
somap = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número[{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
            pares.append(matriz[l][c])
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
somat = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('=' * 50)
print(f'Os números pares digitados são -> {pares}\nE a soma deles é: {somap}')
print('-' * 40)
print(f'A soma dos termos:'
      f'\n[{matriz[0][2]:^5}]'
      f'\n[{matriz[1][2]:^5}]'
      f'\n[{matriz[2][2]:^5}]\n ,que corresponde a 3° coluna da matriz é: {somat}')
print('-' * 40)
print(f'Na linha 2 temos os valores:\n[{matriz[1][0]}][{matriz[1][1]}][{matriz[1][2]}]'
      f'\nE o maior valor desta linha é {maior}')
