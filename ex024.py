#  Programa que lê o nome de uma cidade e diz se ela começa com o nome "SANTO".
'''
# minha solução
cidade = str(input('Digite o nome da cidade: ')).strip()
cidade1 = cidade.split()
print('O nome da cidade começa com SANTO ? True/False ')
print('SANTO' in (cidade1[0].upper()))
'''
# solução do professor

cid = str(input('Digite o nome de sua cidade: ')).strip()
print('O nome da cidade começa com SANTO ? True/False ')
print(cid[:5].upper() == 'SANTO')
