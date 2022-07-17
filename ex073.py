# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
          'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
          'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
          'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=' * 30)
for tab in range(0, 20):
    print(f'{tab + 1}° - {tabela[tab]} ')

print('=' * 30)
print('Os 5 primeiros times.')
print(tabela[:5])  # desse jeito vai vir os elementos das casas.| 0 | 1 | 2 | 3 | 4 | = 5 primeiros

print('=' * 30)
print('Os últimos 4 colocados')
print(tabela[16:])

print('=' * 30)
print('Colocados em Ordem Alfabética')
print(sorted(tabela))

colocação = tabela.index('Chapecoense') + 1
print(f'{colocação}° - Chapecoense')
# professor
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}° posição')  # usa "" para o python intender a indexação.
