#  Crie um programa onde o usuário possa digitar cinco valores numéricos e
#  cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#  No final, mostre a lista ordenada na tela

'''lista = []
cont = 0
for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    cont += 1
    if cont == 1:
        print(f'Primeiro elemento da lista')
        lista.append(n)
    if cont == 2:
        if n > lista[0]:
            print(f'Adicionado no final da lista')
            lista.append(n)
        else:
            print(f'Adicionado na posição 0')
            lista.insert(0, n)
    if cont == 3:
        if n > lista[0] and n > lista[1]:
            print(f'Adicionado no final da lista')
            lista.insert(2, n)
        if n < lista[0] and n < lista[1]:
            print(f'Adicionado na posição 0')
            lista.insert(0, n)
        else:
            print(f'Adicionado na posição 1')
            lista.insert(1, n)
    if cont == 4:
        if n > lista[0] and n > lista[1] and n > lista[2]:
            print(f'Adicionado no final da lista')
            lista.insert(3, n)
        if n < lista[0] and n < lista[1] and n < lista[2]:
            print(f'Adicionado na posição 0')
            lista.insert(0, n)
        if n > lista[0] and n > lista[1] and n < lista[2]:
            print(f'Adicionado na posição 2')
            lista.insert(2, n)
        else:
            print(f'Adicionado na posição 1')
            lista.insert(1, n)
    if cont == 5:
        if n > lista[0] and n > lista[1] and n > lista[2] and n > lista[3]:
            print(f'Adicionado no final da lista')
            lista.insert(4, n)
        if n < lista[0] and n < lista[1] and n < lista[2] and n < lista[3]:
            print(f'Adicionado na posição 0')
            lista.insert(0, n)
        if n > lista[0] and n > lista[1] and n > lista[2] and n < lista[3]:
            print(f'Adicionado na posição 3')
            lista.insert(3, n)
        if n > lista[0] and n > lista[1] and n < lista[2] and n < lista[3]:
            print(f'Adicionado na posição 2')
            lista.insert(2, n)
        if n > lista[0] and n < lista[1] and n < lista[2] and n < lista[3]:
            print(f'Adicionado na posição 1')
            lista.insert(1, n)
print(lista)
'''
# resolução do professor

lista = []
for c in range(0, 5):  # conta de 0 a 4
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  # se for a primeira digitação ou maior que o ultimo da lista
        lista.append(n)  # acrescenta no final da lista
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  # len(lista) pos a lista vai crescendo
            if n <= lista[pos]:
                lista.insert(pos, n)  # insere na posição 'pos' o número 'n'
                print(f'Adicionado na posição {pos} da lista...')
                break  # quando acha a posição do número digitado a sai no while
            pos += 1  # serve pra ir contando e almentando o número do pos até achar a posição do número digitado
print(f'Os valores digitados em ordem foram {lista}')
