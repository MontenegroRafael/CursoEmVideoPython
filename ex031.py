# Programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longos.

dist = float(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    print('Para uma viagem de {}Km sua passagem vai custar \033[1;32mR${:.2f} reais\033[m'.format(dist, dist * 0.50))
else:
    print('Para uma viagem de {}km sua passagem vai custar \033[1;32mR${:.2f} reais\033[m'.format(dist, dist * 0.45))

# resolução do professor. opção simplificada
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da sua sua passagem vai ser R${:.2f} reais'.format(preço))
