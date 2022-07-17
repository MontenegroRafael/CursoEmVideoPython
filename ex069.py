#   Crie um programa que leia a idade e o sexo de várias pessoas.
#   A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#   No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = cont18 = contm = contf20 = 0
while True:
    print('-' * 30)
    print('Novo Cadastro')
    print('-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo[F/M]: ')).strip().upper()[0]
    while sexo not in 'F,M':
        sexo = str(input('Opção invalida. Digite o sexo[F/M]: ')).strip().upper()[0]
    cont += 1
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contm += 1
    if (sexo == 'F') and (idade < 20):
        contf20 += 1
    print('-' * 30)
    op = str(input('Deseja cadastrar mais? [S/N]: ')).strip().upper()[0]
    while op not in 'S,N':
        op = str(input('Opção invalida. Deseja cadastrar mais? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
print('-' * 30)
print('Resumo do cadastro')
print(f'{cont} - Cadastro(s) feitos.')
print(f'{cont18} - Pessoa(s) tem mais de 18 anos.')
print(f'{contm} - Homem(es) cadastrados.')
print(f'{contf20} - Mulher(es) com menos de 20 anos.')
print('-' * 30)
