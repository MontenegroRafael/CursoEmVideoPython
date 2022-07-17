'''
s = ''
while 'F' != s != 'M':
    s = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]  # pega só a primeira letra.
    if s == 'M':
        print('OK! seu sexo é {}.'.format('Masculino'))
    elif s == 'F':
        print('OK! seu sexo é {}.'.format('Feminino'))
'''
# resolução do professor
sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':  # enquanto 'sexo' não tiver dentro de 'MmFf' continue
    sexo = str(input('Informação inválida. Digite seu sexo[M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
