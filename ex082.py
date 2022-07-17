#  Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, crie duas listas extras que vão conter apenas os valores pares e
#  os valores ímpares digitados, respectivamente.
#  Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Dejesa continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'S,N':
        print('-' * 30)
        r = str(input('\033[31mOpção inválida.\033[m\nDeseja continuar? [S/N]: ')).strip().upper()[0]
        print('-' * 30)
    if r == 'N':
        break
print('=' * 30)
print(f'Dos números digitados temos: \n{lista}')
print('=' * 30)
print(f'{par} estes são os números pares digitados')
print('-' * 30)
print(f'{impar} estes são os números ímpares digitados')

