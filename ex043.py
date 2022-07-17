# Programa que lê o peso e altura de uma pessoa e calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:
'''
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

# pesquisar a fórmula do IMC no google - IMC = peso / altura²

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você esta Abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.2f}. Você esta com o Peso Ideal.'.format(imc))
elif imc <30:
    print('Seu IMC é de {:.2f}. Você esta com Sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.2f}. Você esta com Obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Você está com Obesidade Móbida'.format(imc))
