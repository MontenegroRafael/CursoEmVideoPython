# Programa que lê duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

média = (nota1 + nota2) / 2

if média < 5:
    print('\033[31mREPROVADO!\033[m')
    print('Sua média é {}. Para ir para a recuperação o mínimo é 5.0 de média.'.format(média))
elif 5 <= média < 6.9:
    print('\033[33mRECUPERAÇÃO!\033[m')
    print('Sua média é {}. Esta entre 5.0 e 6.9, podendo assim realizar a recuperação.'.format(média))
    print('\033[4mSe prepare, ESTUDE!\033[m')
else:
    print('\033[32mAPROVADO!\033[m')
    print('Sua média é {}. Esta acima de 6.9 e atigiu a média para à aprovação.'.format(média))
    print('\033[7;32m PARABÉNS \033[m')


