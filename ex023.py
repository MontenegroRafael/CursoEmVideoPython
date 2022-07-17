#  Programa que lê um número de 0 à 9999 e mostre na tela cada um dos dígitos separados.
'''
Ex: Digite um número: 1834
> Unidade: 4
> Dezena: 3
> Centena: 8
> Milhar: 1
'''
# tentar fazer via string e via matemática

n = int(input('Digite um número de 0 à 9999: '))
n2 = '{:4}'.format(n)
#n2.split()
#print(n2)
print('Unidade {}'.format(n2[3]))
print('Dezena {}'.format(n2[2]))
print('Centena {}'.format(n2[1]))
print('Milhar {}'.format(n2[0]))

'''
Resposta do professor:

num = int(input('Informe um numero: '))
u = num // 1 % 10  # pega o número digitado faz divisão inteira por 1 e faz o modulo por dez
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Unidade: {}'.format(d))
print('Unidade: {}'.format(c))
print('Unidade: {}'.format(m))

'''

