# Programa que lê o ano de nascimento de um jovem e informa, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar
# Se já passou do tempo do alistamento.

# O programa também deverá mostrar o tempo que falta ou que passou do prazo.
# o Jovem deve se apresentar nos primeiros seis meses do ano em que a idade de 18 é completada.
# sendo assim, entre 01/01 e 30/06

# fazer alteração para caso o usuario seja uma mulher.

import datetime

print('=-' * 40)
print('Consulta de ano de alistamento')
print('=-' * 40)
print('Informe seu sexo:\n1 - para MASCULINO\n2 - para FEMININO')

sexo = int(input('Digite uma opção:  '))

if sexo == 1:
    ano = int(input('Digite o seu ano de nascimento: '))
    hoje = datetime.date.today().year  # usa para buscar somente o ano atual
    idade = hoje - ano

    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, hoje))

    if idade < 17:
        print('Faltam {} ano(s) para você se alistar.'.format(18 - idade))
        print('Seu alistamento é em {}.'.format(ano + 18))
        print('FIQUE ATENTO!')
    elif idade == 17:
        print('PREPARE-SE! \nSEU ALISTAMENTO É {}'.format(hoje + 1))
    elif idade == 18:
        print('CHEGOU A HORA! \nSeu alistamento é neste ano. GO!')
    else:
        print('ALISTAMENTO ATRASADO!')
        print('Já se passou {} ano(s) do seu prazo. Seu ano de Alistamento era {}'.format(hoje - (ano + 18), ano + 18))
elif sexo == 2:
    print('''O alistamento para mulheres não é obrigatório no brasil.
    Caso tenha interesse em ingressar nas força armadas brasileira,
    procure uma unidade do exército, marinha ou aeronáutica para mais informações.''')
else:
    print('Opção inválida')

