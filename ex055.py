# Programa que lê o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
'''
p1 = float(input('Digite o 1° peso: '))
p2 = float(input('Digite o 2° peso: '))
p3 = float(input('Digite o 3° peso: '))
p4 = float(input('Digite o 4° peso: '))
p5 = float(input('Digite o 5° peso: '))

if p2 < p1 > p3 and p4 < p1 > p5:
    print('O peso {} é o maior peso'.format(p1))
elif p1 < p2 > p3 and p4 < p2 > p5:
    print('O peso {} é o maior peso'.format(p2))
elif p1 < p3 > p2 and p4 < p3 > p5:
    print('O peso {} é o maior peso'.format(p3))
elif p1 < p4 > p2 and p3 < p4 > p5:
    print('O peso {} é o maior peso'.format(p4))
else:
    print('O peso {} é o maior peso'.format(p5))

if p2 > p1 < p3 and p4 > p1 < p5:
    print('O peso {} é o menor peso'.format(p1))
elif p1 > p2 < p3 and p4 > p2 < p5:
    print('O peso {} é o menor peso'.format(p2))
elif p1 > p3 < p2 and p4 > p3 < p5:
    print('O peso {} é o menor peso'.format(p3))
elif p1 > p4 < p2 and p3 > p4 < p5:
    print('O peso {} é o menor peso'.format(p4))
else:
    print('O peso {} é o menor peso'.format(p5))
'''
maiorp = 0
menorp = 0
for c in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(c)))
    if c == 1:  # se for o primeiro  laço então o peso digitado assume o maior e o menor
        maiorp = peso
        menorp = peso
    if peso > maiorp:  # depois vai atribuindo novos valor para o maior e o menor peso.
        maiorp = peso
    if peso < menorp:
        menorp = peso
print('O menor peso diditado foi {}Kg.'.format(menorp))
print('O maior peso digitado foi {}Kg.'.format(maiorp))

