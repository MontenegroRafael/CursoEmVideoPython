#s = 'rafael monte'
#print(s[7])

# Aula de Laços de Repetição
'''
for c in range(0, 6): # c é de contador
    print('Oi!') # vai escrever 'oi' 6 vezes. (0,1,2,3,4,5)
    print('FIM')

for c in range(0, 6):
    print(c)  # vai cuntar de 0 a 5. (0,1,2,3,4,5)
print('FIM')

for c in range(0, 7): # o último algorismo do ranger o contador ignora
    print(c)  # vai cuntar de 1 a 6. (1,2,3,4,5,6)
print('FIM')

for c in range(6, 0, -1):
    print(c)  # vai cuntar de 6 a 1. coloca o -1 para ordem decrescente.
    # neste espaços vc informa o que o contador vai fazer (1,2,3,4,5,6)
print('FIM')

for c in range(0, 7, 2):  # de 0 a 6 pulando de dois em dois
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n + 1):  # n + 1 para que faça a contagem até o número digitado.
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s = s + n  # pode escrever no Python s += n
print('O somatório de todos os valores foi {}'.format(s))
'''

#  aula 14

for c in range(1, 10):
    print(c, end=' ')
print('FIM')


c = 1  # contador começa com 1
while c < 10:  # enquanto(while) o contador(c) for menor que 10
    print(c, end=' ')
    c = c + 1
print('FIM')

n = 1  # 'n' começa com 1
while n != 0:  # enquanto 'n' for diferente de 0(zero) execute a linha indentada abaixo. é uma cindição de parada
    n = int(input('Digite um valor: '))
print('FIM')


r = 'S'  # o valor de 'r' começa com 'S'
while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: '))
print('FIM')

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:  # desconcidera o zero para a contagem de números pares.
        if n % 2 == 0:  # estudo de número par
            par = par + 1  # conta quantos numeros pares são digitados
        else:
            impar = impar + 1  # conta quantos numeros pares são digitados
print('{} números Pares e {} números Impares.'.format(par, impar))
'''
'''
cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')

# usando o 'while True:'
# sendo que neste caso está em lup infinito. pois não tem nenhum comando para interromper
cont = 1
while True:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')
'''

# Utilizando o 'while' com o 'break'
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

# novidade das formataçoes 'f' strings

print(f'A soma vale {s}')
print(f'A soma vale {s:-^20}')

'''

#  Variáveis Compostas (Tuplas)
#  () - Tupla
#  [] - lista
#  {} - Dicionário
# Tuplas são Imutáveis
'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  # pode ser escrito sem os parenteses
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])  # sempre vai ser desconciderado o último elemento.

# maneiras de usar o FOR
for cont in range(0, len(lanche)):
    print(f'Você comeu {lanche[cont]}')

for cont in range(0, len(lanche)):
    print(f'Você comeu {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Você comeu {comida}')

for pos, comida in enumerate(lanche):
    print(f'Você comeu {comida} na posição {pos}')

print(sorted(lanche))  # vai mostra organizado A-Z a tupla. pode ser usada para transformar em lista.
print(lanche)
# se colocar um print depois vai perceber que a tupla não mudou, apenas foi um artifício para mostrar na tela


a = (2, 5, 4)
b = (5, 8, 1, 2)
c1 = a + b  # junta as tuplas e forma uma nova
c2 = b + a  # a ordem da operação inporta
print(a)
print(b)
print(c1)
print(c2)
print(len(c1))
print(c1.count(5))  # quantas vezes o número 5 aparece dentro da Tupla 'c1'
print(c1)
print(c1.index(8))  # em que posição esta o número 8 dentro da Tupla 'c1'
print(c1.index(4))  # em que posição esta o número 8 dentro da Tupla 'c1'
print(c1.index(2))  # em que posição esta o número 8 dentro da Tupla 'c1'
# sabemos que tem 2 números 2 então usamos o delocamento pra próxima posição que neste caso será '1'
print(c1.index(2, 1))  # começa apartir da posição 1 já que foi testado que na posição 0 tem um 2
'''

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)  # 'del é usado para deletar uma variável
print(pessoa)


# Listas []
'''
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
print(lanche[3])
lanche[3] = 'Picolé'
print(lanche)
print(lanche[3])
lanche.append('Cokes')  # adciona no final da lista
print(lanche)
lanche.insert(0, 'Cachorro Quente')  # adiciona em qualquer posição empurrando pra frente os demais itens que já existem
print(lanche)
del lanche[2]  # dele o termo pelo número da chave
lanche.pop(4)  # outra forma de deletar pelo número da chave
lanche.pop()  # desta forma com os parenteses vaziu deleta o último elemento.
lanche.remove('Pizza')  # outra opção para deletar, desta vez escrevendo o que tem dentro da chave.
print(lanche)

if 'pizza' in lanche:
    lanche.remove('Pizza')


valores = list(range(4, 11))
print(valores)
valores1 = [8, 2, 5, 4, 9, 3, 0]
valores1.sort()  # organiza os valores  ,  primeiro faz a alteração depois coloca dentro do print
print(valores1)
valores1.sort(reverse=True)  # organiza de forma descrescente
print(valores1)
print(len(valores))  # quantidades de casas
valores1.insert(1, 8)  # vai adicionar o número 8 na casa 1
print(valores1)
valores1.remove(8)  # remore o primeiro 8 somente. para remover mais tem que usar laços
print(valores1)


# valores = list()
# ou
valores = []
valores.append(5)
valores.append(int(input('Digite um número')))
valores.append(4)
for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):  # desta forma ele busca a chave 'c' que esta o valor 'v'
    print(f'\nNa posição {c} encontrei o valor {v}...')
'''

a = [2, 3, 4, 7]
b = a  # desta forma voce liga uma lista na outra. tudo que mexe em um vai mexer na outra
b[2] = 8  # vai auterar a segunda posição em 'a' e 'b' e colocar 8 no lugar
# para que isso não ocorra pode usar a seguinte forma.
b = a[:]  # 'b' vai receber todos os elementos de 'a' e se torna independente.
b[2] = 0
a[2] = 10
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# lista II

teste = list()  # cria uma lista vazia
teste.append('Rafael')  # pede para acrescentar 'Rafael' na lista 'teste'
teste.append(35)
print(teste)
galera = list()  # cria outra lista 'galera'
galera.append(teste[:])  # desta forma pega uma copia do inicio até o fim.
# pode fazer fatiamento de intervalo especifico tambem.
#galera.append(teste)  # se colocar desse jeito cria uma ligação entre as duas lista.
# e o que queremos é somente pegar uma copia dos dados da lista 'teste'
print(galera)

# pode declarar uma lista de uma vez só.
galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera1)
print(galera1[0])
print(galera1[0][0])
print(galera1[2][1])
print(galera1[:])

for p in galera1:
    print(p)
    print(p[0])  # somente mostra o primeiro termo no caso nome
    print(p[1])  # somente mostra o segundo termo no caso nome
    print(f'{p[0]} tem {p[1]} anos de idade')  # mostrar formatado


nomes = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))  # lê e coloca dentro da lista
    dado.append(int(input('Idade: ')))  # lê e coloca dentro da lista
    nomes.append(dado[:])  # cria uma copia de dados dentro da lista de nomes
    dado.clear()  # limpa dados
print(nomes)

totmai = totmen = 0
for p in nomes:
    if p[1] >= 21:  # vai analisar somente o termo 1
        print(f'{p[0]} é maior de idade.')  # responde pegando o termo 0
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

# dicionários

'''
pessoas = {'nome': 'Gustavo', 'Sexo':'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['Sexo']  # apaga a chave 'Sexo'
pessoas['nome'] = 'Leandro'  # troca o valor da chave 'Nome' para 'Leandro'
pessoas['peso'] = 98.5  # adiciona
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []  # criando uma lista 'brasil'
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''

estado = dict()  # criando dicionário 'estado'
brasil = list()  # criando lista 'brasil'
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())  # copia o conteudo de 'estado'
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')


