#  Faça um programa que leia nome e peso de várias pessoas,
#  guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

print(f'{" Pesagem ":=^30}')
temp = []
cadastro = []
maisp = menosp = 0
while True:
    print('-' * 30)
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maisp = menosp = temp[1]
    else:
        if temp[1] > maisp:
            maisp = temp[1]
        if temp[1] < menosp:
            menosp = temp[1]
    cadastro.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'S,N':
        print('*' * 30)
        r = str(input('\033[31mOpção invalida!\033[m\nDeseja continuar? [S/N]:')).strip().upper()[0]
        print('*' * 30)
    if r == 'N':
        break
print('_' * 30)
print(f'{len(cadastro)} pessoa(s) Cadastradas')
for p in cadastro:
    if p[1] == maisp:  # fator de classificação para pessoas mais pesadas
        print(f'As pessoas com maior peso é {p[0]} com {maisp}')
    elif p[1] == menosp:  # fator de classificação para pessoas mais leves
        print(f'As pessoas com menor peso é {p[0]} com {menosp}')
print('_' * 30)
