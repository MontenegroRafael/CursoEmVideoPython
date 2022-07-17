#  Programa que lê uma frase qualquer pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip() #  pela resolução do professor ele já colocar aqui em cima o upper()
print('A letra A aparece {} vez(es)'.format(frase.upper().count('A')))
print('A primeira letra A aparece na {}° posição'.format(frase.upper().find('A') + 1))
print('A última letra A aparece na {}° posição'.format(frase.upper().rfind('A') + 1))
# o r na frente do find faz com que ele comece contando pela direita rigth

