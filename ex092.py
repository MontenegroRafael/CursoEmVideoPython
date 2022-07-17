#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#  cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
#  o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
hoje = datetime.date.today().year  # formula para pegar o ano atual.
#   hoje = datetime.now().year  - outra forma
tempodeapo = 35

cadastro = {'nome': str(input('Nome: ')),
            'ano': int(input('Ano de nascimento: ')),
            'ctps': int(input('N° CTPS(0 não tem): '))}
cadastro['idade'] = hoje - cadastro['ano']
if cadastro['ctps'] != 0:
    cadastro['anocontr'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposenta'] = cadastro['idade'] + ((cadastro['ano'] + tempodeapo) - hoje)
print(cadastro)
print('=' * 30)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}.')



