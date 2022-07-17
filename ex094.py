#  Crie um programa que leia nome, sexo e idade de várias pessoas,
#  guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre:
#  A) Quantas pessoas foram cadastradas
#  B) A média de idade
#  C) Uma lista com as mulheres
#  D) Uma lista de pessoas com idade acima da média

temp = {}
base = []
mulheres = []
acimamediaidade = []
somaidade = 0

while True:
    temp['nome'] = str(input('Nome: '))

    while True:
        temp['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if temp['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    temp['idade'] = int(input('Idade: '))
    somaidade = somaidade + temp['idade']
    base.append(temp)
    resp = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    while resp not in 'S,N':
        print('=' * 40)
        print('Opção Invalida!')
        resp = str(input('Deseja cadastrar outra pessoa? [N/S]:')).strip().upper()[0]
    if resp == 'N':
        break



print(f'{len(base)} pessoas cadastra(s)')
media = somaidade / len(base)
print(f'{media} é a média de idade.')
for c in range(0, len(base)):
    for k, v in base[c].items():
        if v == 'F':
            mulheres.append(base[c])
        if k == 'idade':
            if v >= media:
                acimamediaidade.append(base[c])
print('As mulheres cadastradas foram:')
print(mulheres)
print('Lista das pessoas que estão acima da média:')
print(acimamediaidade)


