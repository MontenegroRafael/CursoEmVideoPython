#  Crie um programa que leia nome e duas notas de vários alunos e
#  guarde tudo em uma lista composta. No final,
#  mostre um boletim contendo a média de cada um e
#  permita que o usuário possa mostrar as notas de cada aluno individualmente.

temp = []
notas = []
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append((temp[1] + temp[2]) / 2)
    notas.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'N,S':
        print('Opção invalida!')
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('=' * 40)
print(f'{"N°":<3}{"NOME":<10}{"MÉDIA":<5}')
print('-' * 30)
for i, n in enumerate(notas):
    print(f'{i + 1:<3} {n[0]:<10} {n[3]:<5.2f}')
while True:
    print('-' * 30)
    print('Deseja rever as notas de algum aluno?')
    op = int(input('Digite o [n°] do aluno desejado ou [0] para encerrar: '))
    print('-' * 30)
    if op == 0:
        print('Programa encerrado!')
        break
    else:
        print(f'As notas de {notas[op - 1][0]} são {notas[op - 1][1:3]}')
print('Volte Sempre!')
