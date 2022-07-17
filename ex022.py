# Prgrama que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas as letras minúsculas.
# > Quantas letras ao todo (sem espaços).
# > quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo -> ')).strip()  # o 'strip' esta ai para tirar os espaços inuteis do inicio e do final do nome
print('=' * 80)
print('Todas as letras Maiúsculas - > {}'.format(nome.upper()))
print('Todas as letras Minúsculas - > {}'.format(nome.lower()))
nome1 = nome.split()
print('_' * 40)
nome2 = '-'.join(nome1)
#print(nome2)
#print(nome2.count('-'))
espaços = nome2.count('-')
print('{} letras ao todo(sem contar os espaços)'.format(len(nome2) - espaços))
print('{} tem {} letras'.format(nome1[0], len(nome1[0])))

# resolução do professor
print('{} letras ao todo(sem contar os espaços)'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
# o find vai dizer a posição do primeiro espaço ' '.
# como começa a contagem de 0 então vai dar o número de letra da primeira palavra.


# outra tentativa
'''print('{} --> {} letra(s)'.format(nome1[0], len(nome1[0])))
print('{} --> {} letra(s)'.format(nome1[1], len(nome1[1])))
print('{} --> {} letra(s)'.format(nome1[2], len(nome1[2])))
print('{} --> {} letra(s)'.format(nome1[3], len(nome1[3])))
print('{} --> {} letra(s)'.format(nome1[4], len(nome1[4])))

print('_' * 40)
print('Total {} letras (sem contar os espaços)'.format(len(nome1[0] + nome1[1] + nome1[2] + nome1[3] + nome1[4])))
'''
