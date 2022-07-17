#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


lista = ('Aprender',
         'Programar',
         'Linguagem',
         'Python',
         'Curso',
         'Gratis',
         'Estudar',
         'Praticar',
         'Trabalhar',
         'Mercado',
         'Programador',
         'Futuro',)

for v in lista:
    print(f'\nNa palavra {v.upper()} temos as vogais: ', end='')
    for letras in v:  # assim vc estuda cada letra dentro de cada palavra que 'v' recebe
        if letras.lower() in 'aeiou':
        # pode colocar acentos aqui dentro para intentificar palavra com acentos
            print(f'\033[34m{letras.lower()}\033[m', end='')
