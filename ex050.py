# Programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for ímpar, desconsidere-o

soma = 0
cont = 0
for c in range(1, 7):
    # Ler 6 números inteiros
    num = int(input('Digite o {}° valor: '.format(c)))
    # não precisa atribuir 6 variaveis.. neste caso vai fazendo a rotina toda em cada laço.
    # o valor de num = vai ficar registrado o ultimo valor
    # somando apenas valores que sejam pares
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Foi digitado {} números PARES e a soma deles é {}.'.format(cont, soma))

