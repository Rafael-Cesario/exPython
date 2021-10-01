#while not
sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Digite M para masculino ou F para feminino')
    sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
print('\033[34m', sexo)
