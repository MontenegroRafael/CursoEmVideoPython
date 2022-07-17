#  Programa que lê a velocidade de um carro.
#  se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$ 7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade do carro em Km/h: '))
if vel > 80:
    print('\033[1;31;40mMULTADO!\033[m - Velocidade ultrapassa o limíte permitido.')
    print('\033[4mA velocidade permitida é 80Km.\033[m {} Km/h excedido.'.format(vel - 80))
    print('\033[1;31mR${:.2f}\033[m de multa.'.format((vel - 80) * 7))
else:
    print('OK! Velocidade dentro dos limítes permitidos')

# o professor fez sem usar o else. colocando o último print alinhado com a borda.