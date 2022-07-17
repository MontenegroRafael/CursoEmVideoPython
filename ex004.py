# programa que leia algo e mostre as informações de tipo primitivo do valor digitado.

# vd = Valor digitado

vd = input('Digite qualquer coisa ')
print(' .{:-^20}. '.format(vd))
print('Tipo primitivo = ', type(vd))  # identifica o tipo primitivo
print('É alfabético - ', vd.isalpha())  # identifica se é alfabético
print('É numérico - ', vd.isnumeric())  # ... se é numérico
print('É alphanumeric - ', vd.isalnum())  # ... se é alfanumérico
print(vd.isascii())  # ... se é
print(vd.isdigit())
print(vd.isdecimal())
print(vd.isidentifier())
print('Esta em minúsculo - ', vd.islower())  # ... se é minusculo
print(vd.isprintable())
print('É somente espaço - ', vd.isspace())
print('Esta capitalizada - ', vd.istitle())  # ... se tem a primeira letra maiúscula
print('Esta em maiúscula - ', vd.isupper())  # ... se tem todas as letra maiúscula