#  Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[], [], []]
cont = 0
for m in range(0, 9):
    cont += 1
    if cont <= 3:
        matriz[0].append(int(input(f'Digite um valor para [0,]:')))
    if 3 < cont <= 6:
        matriz[1].append(int(input(f'Digite um valor para [1,]:')))
    if 6 < cont <= 9:
        matriz[2].append(int(input(f'Digite um valor para [2,]:')))

print(f'[{matriz[0][0]:^4}][{matriz[0][1]:^4}][{matriz[0][2]:^4}]')
print(f'[{matriz[1][0]:^4}][{matriz[1][1]:^4}][{matriz[1][2]:^4}]')
print(f'[{matriz[2][0]:^4}][{matriz[2][1]:^4}][{matriz[2][2]:^4}]')
'''

# resolução do professor

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # já coloca a matriz completa.
for linha in range(0, 3): #  faz um for passando por 0 1 2 representando as linhas
    for coluna in range(0, 3): #  faz um for passnado por 0 1 2 representando as colunas
        #  de pois vai substituindo os valores que estão na matriz. matriz[linha tal][coluna tal] = número digitado
        matriz[linha][coluna] = int(input(f'Digite um número para o endereço [{linha},{coluna}]: '))
for linha in range(0, 3):  #  depois passa novamente com um for para mostrar cada número das linhas
    for coluna in range(0, 3): #  depois passa novamente com um for para mostrar cada número das colunas
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
