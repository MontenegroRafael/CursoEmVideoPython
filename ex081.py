#  Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, mostre:
#  A) Quantos números foram digitados.
#  B) A lista de valores, ordenada de forma decrescente.
#  C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input(f'Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'S,N':
        r = str(input('Opção invalida: Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'{len(lista)} número(s) digitados')
print(f'Em ordem crescente {sorted(lista)}')
lista.sort(reverse=True)
print(f'Em ordem decrescente {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado e não esta na lista.')

