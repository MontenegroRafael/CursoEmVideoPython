# Programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

valorc = float(input('Digite o valor da casa R$: '))
sal = float(input('Digite o valor de seu salário R$: '))
anos = float(input('Digite em quantos anos quer pagar: '))

parcela = valorc / (anos * 12)   #  depois verificar a questão do float se esta dando certo

if sal * 0.30 > parcela:
    print('\033[32mAPROVADO!\033[m')
    print('O valor da parcela será - R${:.2F} x {} meses.'.format(parcela, (anos * 12)))
else:
    print('\033[31mNEGADO!\033[m', end='')  #  para que continue tudo em uma linha só usa o < , end='' >
    print('O valor da parcela será - R${:.2F} x {} meses.'.format(parcela, (anos * 12)))

# resolução do professor

mínimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorc, anos), end='')
print(' a prestação será de R${:.2f}'.format(parcela))
if parcela <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
