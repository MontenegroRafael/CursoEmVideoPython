# Programa que leia as duas notas de um aluno, calcule e mostre a média.

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
média = (nota01 + nota02) / 2

print('A média das notas é {:.1f}'.format(média))  # :.1f para colocar apenas 1 casa depois do ponto.
