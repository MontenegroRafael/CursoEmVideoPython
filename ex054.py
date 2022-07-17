# Programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.
# considere a maioridade 21 anos

import datetime
hoje = datetime.date.today().year  # estou pegando o ano atual. puxa a data de hoje e pega somente o ano.
cmaior = 0
cmenor = 0
for c in range(1, 8):
    num = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(c)))
    if (hoje - num) >= 21:
        cmaior = cmaior + 1
    else:
        cmenor = cmenor + 1
print('{} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade.'.format(cmaior, cmenor))
