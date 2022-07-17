# Programa que lê dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print('O primeiro valor digitado({}) é maior que o segundo({}).'.format(num1, num2))
elif num1 < num2:
    print('O segundo valor digitado({}) é maior que o primeiro({}).'.format(num2, num1))
elif num1 ==num2:
    print('O primeiro valor digitado({}) e o segundo valor digitado({}) são iguais.'.format(num1, num2))
else:
    print('Valor digitado incompativel, tente novamente.')
