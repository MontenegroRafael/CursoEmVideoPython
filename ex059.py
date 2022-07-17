# Programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


finalizar = False
while not finalizar:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    print('=' * 40)
    print('O que deseja fazer com os valores digitados? \nEscolha uma opção abaixo:')
    print(''' 
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        ''')
    op = int(input('Digite o número da opção escolhida: '))
    print('=' * 40)
    while op != 4:
        if op == 5:
            print('Programa finalizado!')
            finalizar = True
            op = 4
        else:
            if op == 1:
                soma = num1 + num2
                print('Opção escolhida [1] - SOMAR')
                print('{} + {} = {}'.format(num1, num2, soma))
                print('=' * 40)
                op = int(input('Escolha outra opção ou aperte [5] para finalizar: '))
            elif op == 2:
                mult = num1 * num2
                print('Opção escolhida [2] - MULTIPLICAR')
                print('{} * {} = {}'.format(num1, num2, mult))
                print('=' * 40)
                op = int(input('Escolha outra opção ou aperte [5] para finalizar: '))
            elif op == 3:
                if num1 > num2:
                    maior = num1
                else:
                    maior = num2
                print('Opção escolhida [3] - MAIOR')
                print('Entre {} e {}. O maior é {}'.format(num1, num2, maior))
                print('=' * 40)
                op = int(input('Escolha outra opção ou aperte [5] para finalizar: '))
            elif (op != 1) or (op != 2) or (op != 3) or (op != 4) or (op != 5):
                print('Opção Invalida. ')
                print('=' * 40)
                op = int(input('Digite o número da opção escolhida: '))

#  resolução do professor

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opção = int(input('>>>>> qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} * {} é '.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando. . .')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')




