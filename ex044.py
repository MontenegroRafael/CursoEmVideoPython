# Programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
'''
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x uo mais no cartão: 20% de juros.
'''
print('=-' * 40)
print(' Cálculo de desconto.')
print('=-' * 40)
preço = float(input('Digite o preço do produto: R$ '))
print('-' * 40)
print('Escolha uma opção abaixo:\nFormas de pagamento')
print('1 - À vista com dinheiro ou cheque\n2 - À vista no cartão\n3 - parcelado no cartão no cartão')
escolha = int(input('>>>>>>>  '))
if escolha == 1:
    print('Para pagamento à vista com dinheiro ou cheque,', end='')
    print(' o desconto é de 10%.')
    print('\033[1;32mR${:.2f}\033[m Preço normal\n\033[1;32mR${:.2f}\033[m Preço com 10% de desconto.'.format(preço, preço - (preço * 0.10)))
elif escolha == 2:
    print('Para pagamento à vista no cartão,', end='')
    print(' o desconto é de 5%.')
    print('\033[1;32mR${:.2f}\033[m Preço normal\n\033[1;32mR${:.2f}\033[m Preço com 5% de desconto.'.format(preço, preço - (preço * 0.05)))
elif escolha == 3:
    parcelas = int(input('Digite o número de parcelas em que deseja pagar: '))
    if parcelas == 2:
        print('Para pagamento em até 2x no cartão,', end='')
        print(' não tem desconto e não entra juros no parcelamento.')
        print('\033[1;32mR${:.2f}\033[m em 2x de \033[1;32mR${:.2f}\033[m Sem juros.'.format(preço, preço / 2))
    elif parcelas > 2:
        print('Para pagamento pracelado apartir de 3x ,', end='')
        print(' incide Juros de 20%.')
        print('\033[1;32mR${:.2f} Preço normal\033[m\n{}x de \033[1;32mR${:.2f}\033[m.'.format(preço, parcelas, (preço + (preço * 0.20)) / parcelas))
        print('Totalizando \033[1;32mR${:.2f}\033[m'.format(preço + (preço * 0.20)))
    elif parcelas < 2:
        print('Para pagamento à vista no cartão,', end='')
        print(' o desconto é de 5%.')
        print('\033[1;32mR${:.2f}\033[m Preço normal\n\033[1;32mR${:.2f}\033[m Preço com 5% de desconto.'.format(preço, preço - (preço * 0.05)))
else:
    print('Opção invalida. Número digitado não corresponde a nunhuma forma de pagamento.\nTente novamente.')
