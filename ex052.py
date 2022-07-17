# Programa que leia um número inteiro e diga se ele é ou não um número primo.
#  Um número primo é aquele que é dividido apenas por um e por ele mesmo.
#  Um número é classificado como primo se ele é maior do que um e é divisível apenas por um e por ele mesmo.
#  Apenas números naturais são classificados como primos.

'''
num = int(input('Digite um número:  '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m')
        cont = cont + 1
    else:
        print('\033[m')
vezes = cont
if vezes <= 2:
    print('Este número é PRIMO! ')
else:
    print('Não é um número PRIMO! ')

#print(c, end=' ')
#print('O número {} é dividido {} vezes.'.format(num, cont))
'''

num = int(input('Digite um número:  '))  # - lê o número
tot = 0  # --------------------------------- Começa a variável com zero

for c in range(1, num + 1):  # -------- cria uma variável 'c' que vai percorrer um intervalo de '1' a 'num+1'
    if num % c == 0:  # --------------- se 'num' tiver resto zero quando dividido por 'c'. execute as linhas dentro deste 'if'
        print('\033[33m', end=' ')  # - uso de cores

        tot = tot + 1  # - 'tot' é um contador que vai contabilizando toda vez que esta condição 'if' for verdadeira.
    else:  # ------------- se não execute as linhas dentro deste 'else'

        print('\033[31m', end=' ')  # - uso de cores
    print('{}'.format(c), end=' ')  # - mostra a sequencia da variável 'c' criada pelo laço 'for' para o 'num' digitado.

print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))  # - mostra o resultado para 'num' e 'tot'
if tot == 2:  # - se quantidade de vezes'tot' que o primeiro 'if' foi verdade for igual a 2. execute as linhas dentro deste' if'
    print('E por isso ele É PRIMO!')
else:  # - se não execute as linha abaixo deste 'else'
    print('E por isso ele NÃO É PRIMO!')
