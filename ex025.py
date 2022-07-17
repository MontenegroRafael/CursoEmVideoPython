#  Programa que lê o nome de uma pessoa e diz se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: '))
print('O nome digitado pussue SILVA? true/false')
nome1 = nome.upper().split()
print('SILVA' in nome1[:])
print(nome1)

# resolução do professor

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

