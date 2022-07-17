# programa que lê um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# >1 para binário
# >2 para octal
# >3 para hexadecimal

#estudar base numéricas

print('\033[1;36m=-\033[m' * 40)
print('\033[7m{:^80}\033[m'.format('CONVERSOR DE BASE NUMÉRICA'))
print('\033[1;36m=-\033[m' * 40)

n = int(input('Digite um número inteiro: '))
print('=' * 80)
print('Escolha a opção para conversão:\nDigite;\n\033[36m1 para BINÁRIO\n2 para OCTAL\n3 para HEXADECIMAL\033[m')
print('=' * 80)
op = int(input('Opção >>> '))

if op == 1:
    print('({})decimal = ({})binário'.format(n, bin(n)[2:]))
    # usa o fatiamento para tirar os dois primeiro digitos (a variável)[inicio:fim]
elif op == 2:
    print('({})decimal = ({})octal'.format(n, oct(n)[2:]))
elif op == 3:  # não pode usar o else aqui porque. precisa dar a opção invalida.
    print('({})decimal = ({}) hexadecimal'.format(n, hex(n)[2:]))
else:
    print('Opção inválida.')
