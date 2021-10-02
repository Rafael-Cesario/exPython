#Banco de dados
maior_18 = 0
h = 0
m = 0
while True:
    #diga o sexo
    while True:
        print('\033[34m-='*20, '\033[m')
        sexo = str(input('Sexo [M/F]: ')).strip()[0].upper()
        if sexo in 'MmFf':
            break
        else:
            print('\033[31mSexo: Valor invalido, digite novamente\033[m')
    if sexo in 'Mm':
        h += 1
    #diga a idade
    idade = int(input('Idade: '))
    if idade > 18:
        maior_18 +=1 
    if sexo in 'Ff':
        if idade < 20:
            m += 1
    #quer continuar
    while True:
        continuar = str(input('Continuar [S/N]: ')).strip()
        if continuar in "NnSs":
            break
    if continuar in 'Nn':   
        break
print(f'\nMais de 18 anos: {maior_18}')
print(f'Homens: {h}')
print(f'Mulheres com menos de 20: {m}')
