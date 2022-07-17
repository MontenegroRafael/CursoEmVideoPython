#  Escreva um programa que leia um número N inteiro qualquer e
#  mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#  Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

#  É uma sucessão de números que aparecem codificada em muitos fenômenos da natureza.
#  Descrita no final do século 12 pelo matemático italiano Leonardo Fibonacci,
#  ela é infinita e começa com 0 e 1. Os números seguintes são sempre a soma dos dois números anteriores.
#  Portanto: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34…

print('{:-^40}'.format(' Sequência de Fibonacci '))
n = int(input('Digite o número de termos que deseja ver: '))
termo = 0
termo1 = 0
termo2 = 1
cont = 1
while cont <= n:
    print(' {} '.format(termo), end='-')
    cont = cont + 1
    termo1 = termo2
    termo2 = termo
    termo = termo1 + termo2
print(' FIM')

