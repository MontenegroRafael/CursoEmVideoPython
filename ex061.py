#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

#  10° termo = primeiro termo'+('10° termo - 1) * 'razão'
'''
pri = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
print(pri, end=' ')
c = pri
while c != (pri + (10 - 1) * razão):
    c = c + razão
    print(c, end=' ')
'''
# resolução do professor

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('FIM!')