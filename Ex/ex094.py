#guarde dicionarios em uma lista, leia o nome, idade, sexo, de varias pessoas. mostre quantas pessoas foram cadastradas, a média de idade, uma lsita com mulheres, uma lista com idade acima da média.
print('\033[34m')
pessoas = list()
pessoa = dict()
mulheres = list()
mmedia = list()
total = 0
while True:
    #nome
    pessoa['Nome'] = str(input('Nome: '))
    #idade
    pessoa['Idade'] = int(input('Idade: '))
    total += pessoa['Idade']
    #sexo
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
        if pessoa['Sexo'] in 'MF':
            break
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    pessoas.append(pessoa.copy())
    pessoa.clear()
    #continuar
    while True:
        c = str(input('Continuar [S/N]: ')).strip().upper()
        if c in "SN":
            break
    if c in "N":
        break
media = total / len(pessoas)
print(pessoas)
print('-='*20)
print(f'Pessoas cadastradas: {len(pessoas)} pessoas.')
print(f'A média de idade é: {media:.1f}')
print(f'As mulheres cadastradas são: {mulheres}')
print('As pessoas com idade acima da média são: ')
for p in pessoas:
    if p['Idade'] >= media:
        for k,v in p.items():
            print(f'{k}: {v}', end=' ')
        print()