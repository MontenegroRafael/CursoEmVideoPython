# Programa que lê o primeiro termo e a razão de uma PA( progreção aritimética).
# No final, mostre os 10 primeiros termos dessa progressão.
print('\033[34m=\033[m' * 38)
print('  {:^40}'.format('\033[35m10 TERMOS DE UMA PA\033[m'))
print('\033[34m=\033[m' * 38)

termo1 = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = termo1 + (10 - 1) * razão  # fórmula matemática para achar o 10n termo de uma PA. 'primeiro termo'+('termo desejado - 1) * 'razão'
for c in range(termo1, décimo + razão, razão):  # décimo+razão para chegar ao 10 primeiro elementos
    print('{}'.format(c), end='-')
print('ACABOU!')
