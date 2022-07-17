#   Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#   O programa vai ler o nome do jogador e quantas partidas ele jogou.
#   Depois vai ler a quantidade de gols feitos em cada partida.
#   No final, tudo isso será guardado em um dicionário, incluindo o
#   total de gols feitos durante o campeonato.

gols = []
total = 0
print(f'{" Aproveitamento de jogos ":=^51}')
cadastro = {'nome': str(input('Nome: '))}
cadastro['partidas'] = int(input(f'Quantas partidas {cadastro["nome"]} jogou? : '))
for n in range(0, cadastro['partidas']):
    gols.append(int(input(f'Digite quantos gols marcados da {n + 1}° partida.: ')))
    total = total + gols[n]
cadastro['gols'] = gols[:]
cadastro['total'] = total
#  poderia ser - cadastro['total'] = sum(gols)
print('=' * 51)
print(cadastro)
print('=' * 51)
for k, v in cadastro.items():
    print(f'O campo {k} tem valor {v}.')
print('=' * 51)
print(f'O jogador {cadastro["nome"]} jogou {cadastro["partidas"]} partidas.')
for i, v in enumerate(cadastro['gols']):
    print(f' => Na patida {i + 1}, fez {v} gols.')
print(f'Foi um total de {total} gols.')
