#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
#  na ordem correta.

exp = input('Digite uma expressão qualquer: ')
esq = exp.count('(')
dir = exp.count(')')
for c in exp:
    if (c == exp[0] and c == ')') or (esq != dir) or (c == exp[len(exp)-1] and c == '('):
        print('Sua expressão não é válida! REVISE')
        break
    else:
        print('Sua expressão é válida!')
        break
'''
# outra opção minha.
esq = exp.count('(')
dir = exp.count(')')
if esq == dir:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida! REVISE')
'''
# solução do professor

expr = str(input('Digite a expressão'))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')  # acescenta um parentese abrindo na lista
    elif símb == ')':
        if len(pilha) > 0:  # se a lista não estiver vazia
            pilha.pop()  # retira um elemento da lista
        else:
            pilha.append(')')  # se não acrescenta uma parentese fechando
            break
if len(pilha) == 0:  # se no final não sobrar nada na lista então é valida a expressão.
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
