# Programa que lê um ano qualquer e mostre se ele é BISSEXTO.

# ano é Bissexto quando dividido por 4 resta 0
# exceto anos múltiplos de 100 ou que não são mútiplos de 400

import datetime

ano = int(input('Digite com 4 digitos um ano qualquer: '))
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print('\033[4;36mO ano {} é Bissexto\033[m'.format(ano))
else:
    print('\033[4;34mO ano {} não é Bissexto\033[m'.format(ano))
print('_' * 40)
datahoje = datetime.date.today().year

if (datahoje % 4) == 0 and (datahoje % 100) != 0 or (datahoje % 400) == 0:
    print('Como estamos no ano {}, o próximo ano bissexto será {}'.format(datahoje, datahoje + 4))
if ((datahoje + 1) % 4) == 0 and (datahoje % 100) != 0 or (datahoje % 400) == 0:
    print('Como estamos no ano {}, o próximo ano bissexto será {}'.format(datahoje, datahoje + 1))
if ((datahoje + 2) % 4) == 0 and (datahoje % 100) != 0 or (datahoje % 400) == 0:
    print('Como estamos no ano {}, o próximo ano bissexto será {}'.format(datahoje, datahoje + 2))
else:
    print('Como estamos no ano {}, o próximo ano bissexto será {}'.format(datahoje, datahoje + 3))

# bonus do professor.
# como fazer o python descobrir o ano atual da máquina.
# datetime.date.today().year - desta format busca a data atual e pega só o ano(year)
