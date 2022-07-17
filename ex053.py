# Programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# palindromo é a palavra que tem o moesmo sentido quando lemos de trás pra frente tambem.
'''
Ex. Apos a sopa
Natan
A sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''

# lê a frase e retira os epaços do início e do final
# - coloca todas as letras em maiúsculo
frase = str(input('Digite uma frase.')).strip().upper().split()
frase = ''.join(frase) # junta as palavra sem usar nada entre elas''
fraserev = frase[::-1]  # vai ler a frase do inicio até o final só que subitraindo a casa por causa do'-1'
print('A frase {} fica invetida {}.'.format(frase, fraserev))

if frase == fraserev:
    print('Esta frase é um PALINDROMO!')
else:
    print('Esta frase NÃo é um palindromo!')

frase = str(input('Digite uma frase: ')).strip().upper()  # lê a frase tira os espaços inuteis e coloca em maiúsculo
palavras = frase.split()   # separa em palavras
junto = ''.join(palavras)  # junta as palavras sem os espaços
inverso = ''  # começa o somatorio de inverso em vazio ''
for letra in range(len(junto) -1, -1, -1):  # range de ('quantidade de letras'(da variável junto) -1) até o zero. subtraindo uma casa 'por isso o -1'
    inverso += junto[letra]  # somatorio de inverso começando em vazio
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
