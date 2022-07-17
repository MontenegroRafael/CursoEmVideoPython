# Programa que pergunte o salário de um funcionário e cacule o valor do seu aumento.

# para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os salários inferiores ou iguais, o aumento é de 15%

salário = float(input('\033[7;30;42mDigite o valor do Salário: R$:\033[m '))

if salário > 1250.00:
    print('Seu salário vai aumentar \033[4m10%\033[m e vai ficar:\n \033[4;32mR${:.2f}\033[m.'.format(salário + (salário * 0.10)))
else:
    print('Seu salário vai aumentar \033[4m15%\033[m e vai ficar:\n \033[4;32mR${:.2f}\033[m'.format(salário + (salário * 0.15)))
print('\033[1;32mPARABÉNS\033[m')

# RESOLUÇÃO DO PROFESSOR

if salário < + 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a guanhar R${:.2f}'.format(salário, novo))
