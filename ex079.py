#  Crie um programa onde o usuário possa digitar vários valores numéricos e
#  cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = []
while True:
    n = int(input('Digite um número: '))
    print('=' * 30)
    if n in valores:
        while n in valores:
            n = int(input(f'Este número já consta na lista.\n{valores}\nPor favor digite outro número: '))
            print('=' * 30)
    valores.append(n)
    op = str(input(f'\033[34mSua lista já contém os números: {valores}\nDeseja adicionar mais? [S/N]: \033[m')).strip().upper()[0]
    print('=' * 30)
    while op not in 'S,N':
        op = str(input('Opção invalida!\nDeseja adicionar mais? [S/N]: ')).strip().upper()[0]
        print('=' * 30)
    if op == 'N':
        break
print(f'\033[31mSua lista em ordem crescente - {sorted(valores)}\033[m')
print('=' * 30)
'''
#  resolução professor

números = []
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('número cadastrado com sucesso')
    else:
        print('Número repetido. Não cadastrado')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
números.sort()
print(f'Você digitou os valores {números}')
