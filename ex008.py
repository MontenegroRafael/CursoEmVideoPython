# Programa que leia um valor em metros e o exiba em centimetros e milimetros.
# na resolução teve novo desafio para outras unidades de medidas.

vm = int(input('Digite o valor em metros: '))

km = vm * 0.001
hm = vm * 0.01
dam = vm * 0.1

dm = vm * 10
cm = vm * 100
mm = vm * 1000

print('{} centimetros'.format(km))
print('{} centimetros'.format(hm))
print('{} centimetros'.format(dam))
print('=' * 80)
print('{} metro(s) é igual a:'.format(vm))
print('=' * 80)
print('{} centimetros'.format(dm))
print('{} centimetros'.format(cm))
print('{} milimetros'.format(mm))
