#  Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
#  de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
#  mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
op = 'S'
while op != 'N':
    núm = int(input('Digite um número de 0 à 20: '))
    while núm < 0 or núm > 20:
        núm = int(input('Número inválido. Digite um número de 0 à 20: '))
    print(f'O número digitado foi o {extenso[núm]}.')
    op = str(input('Deseja executar novamente? [S/N]: ')).strip().upper()[0]
    while op not in 'S,N':
        op = str(input('Opção inválida.Deseja executar novamente? [S/N]: ')).strip().upper()[0]
print('FIM!')
#  Resolução do professor
'''
while True:
    núm = int(input('Digite um número entre 0 e 20: ')
    if 0 <= núm <= 20:
        break
    print('Tente novamente.', end='')
    
print(f'Você digitou o número {extenso[núm]}
'''

