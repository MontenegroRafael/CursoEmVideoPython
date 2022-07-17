#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.

#  Lê o primeiro termo
primeiro = int(input('Digite o primeiro termo da PA: '))
#  lê a razão
razão = int(input('Digite a razão da PA: '))

#  variáveis
termo = primeiro  # assume que termo é igual a primeiro para que começe mostrando o primeiro termo
cont = 1  # assume 1 pois já começa com o primeiro termo expresso. então quando faz o 1° cálculo já mostrou 2 termos
total = 0  # assume 0 pra começar mostrando 10 termos por conta da formula 'total = total + mais
mais = 10  # assume 0 pra começar mostrando 10 termos
while mais != 0:  # enquanto mais for diferente de zero execute
    total = total + mais  # define o numero de termos que vai ser expresso
    while cont <= total:  # enquanto 'cont' for menor igual a total execute. é menor igual pois para mostra o 10° termo
        print('{}'.format(termo), end=' ')  # já começa mostrando o primeiro termo e depois vai mostrando o resultado da formula
        termo += razão  # formula
        cont += 1  # contador de termo ue já começa com 1 pois já foi expresso o primeiro termo
    print('PAUSA')
    # atribui novo valor pra 'mais' por isso estar indentado afrente de mais antigo
    # valida novamente a condição do while != 0
    # e entra no laços novamente do while cont<=total atribuindo novo valor para 'total'
    mais = int(input('Quantos termos você quer mostrar a mais? '))
# vai ser mostrado se a condição de while != 0 não for feita.
print('Pregressão finalizada com {} termos mostrados.'.format(total))




