# Progrma que converta uma temperatura digitada em °C(Celsius) e converta para °F(Farenheits).

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32 # pode usar esta forma sem parentese pois a ordem de precedentes permite.
# a formula para esa converção é  ((9 * °C) / 5) + 32

print('=' * 40)
print('{:.1f}°C é igual a {:.1f}°F'.format(c, f))
