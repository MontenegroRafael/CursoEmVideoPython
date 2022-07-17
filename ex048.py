# Programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        cont = cont + 1  # um contador faz sempre + 1. pois vai contando os elementos
        soma = soma + c  # um acumulador faz sempre + (variarel) pois vai acumulando.
print(soma)
print(cont)
