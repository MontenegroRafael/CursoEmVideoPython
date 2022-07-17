# Programa que leia a comprimento e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessaria para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².

c = float(input('Digite a comprimento em metro(m) '))
a = float(input('Digite a altura em metros(m) '))

area = c * a

print('=' * 80)
litros = int((area / 2) + 1)
# coloquei + 1 pra conpensar quando resultar em número quebrado e assim não fatar tinta.
# E ter sempre um numero inteiro como resposta

print('{} m² de área a ser pintada. '.format(area))
print('{} litro(s) necessario(s) para pintar toda a área. '.format(litros))
