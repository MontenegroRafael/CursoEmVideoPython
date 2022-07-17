#  Crie um programa que simule o funcionamento de um caixa eletrônico.
#  No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
#  o programa vai informar quantas cédulas de cada valor serão entregues.
#  OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('{:-^30}'.format('Banco Du Sêuze.'))
while True:
        valor = int(input('Digite o valor para saque. R$: '))
        if valor >= 50:
            cinq = valor // 50
            valor = valor - (50 * cinq)
            print(f'Total de {cinq} cédulas de R$50.')
        if valor >= 20:
            vint = valor // 20
            valor = valor - (20 * vint)
            print(f'Total de {vint} cédulas de R$20.')
        if valor >= 10:
            dez = valor // 10
            valor = valor - (10 * dez)
            print(f'Total de {dez} cédulas de R$10.')
        if valor >= 1:
            um = valor // 1
            valor = valor - (1 * um)
            print(f'Total de {um} cédulas de R$1.')
        if valor == 0:
            break
print('Volte Sempre!')
'''
#  Resolução do professor

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50 # variável começa com 50 que neste caso é a nota mais alta
totcéd = 0 # contador para total de cédulas. para saber quantas cédulas vai ser de cada valor.
while True:
    if total >= céd:
        total = total - céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Volte Sempre!')
for c in range(0, 5):
    print(c)
