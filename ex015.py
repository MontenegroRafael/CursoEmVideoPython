# Programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.

kmp = float(input('Quantos Km percorridos? '))
dal = int(input('Quantos dias de aluguel? '))
custo = (60 * dal) + (kmp * 0.15)
print('=' * 40)
print('{} dias de aluguel \n{} Km percorridos'.format(dal, kmp))
print('')
print('R$ {:.2f} Total a pagar'.format(custo))
