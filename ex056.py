# programa que lê o Nome, Idade e Sexo de 4 pessoas. No final do programa, mostre:
'''
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

cont = 0
soma = 0
idademaior = 0
idademenor = 0
nomemaior = ''
nomemenor = ''
somamu = 0
for c in range(1, 5):
    print('Dados da {}° Pessoal: '.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
#  fazendo a média das idades digitadas.
    cont = cont + 1
    soma = soma + idade
#  buscando o nome do HOMEM mais velho.
    if (c == 1) and (sexo == 'M'): # pode usar - sexo in 'Mm' - assim não precisa usar o upper() lá em cima.
        nomemaior = nome
        nomemenor = nome
        idademaior = idade
        idademenor = idade
    if (sexo == 'M') and idade > idademaior:
        idademaior = idade
        nomemaior = nome
    if (sexo == 'M') and idade < idademenor:
        idademenor = idade
        nomemenor = idade
    elif sexo == 'F' and idade < 20:
        somamu = somamu + 1
print('A média das idades digitadas é {}'.format(soma / cont))
print('O homem mais velho é {} pois tem {} anos.'.format(nomemaior.title(), idademaior))
print('O homem mais novo é {} pois tem {} anos.'.format(nomemenor.title(), idademenor))
print('Dos nome digitados exitem {} mulheres com menos de 20 anos.'.format(somamu))
