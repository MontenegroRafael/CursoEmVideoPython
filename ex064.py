# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Soma infinita')

cont = 0
total = 0
finalizar = False
while not finalizar:
    n = int(input('Digite um número: '))
    while n != 999:
        total = total + n
        cont = cont + 1
        n = int(input('Digite 999 se quiser finalizar \nou \nDigite um número: '))
    if n == 999:
        finalizar = True
    print('Soma finalizada. Foram digitados {} números'.format(cont))
    print('A somatória de todos os valores é {}'.format(total))

# Resolução do professor

núm = cont = soma = 0
núm = int(input('Digite um número [999 para finalizar]: '))
# colocou a variale num também fora para parar o laço quando digitar 999 sem que 999 entre na soma ou contagem
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para finalizar]: '))

print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
