#leia o nome e peso de varias pessoas
print('\033[34m')
pessoas = []
np = []
maior = menor = 0
while True:
    np.append(str(input('Nome: ')))
    np.append(int(input('Peso: ')))
    pessoas.append(np[:])
    if len(pessoas) == 1:
        maior = menor = np[1]
    else:
        if np[1] > maior:
            maior = np[1]
        if np[1] < menor:
            menor = np[1]
    np.clear()
    c = str(input('Continuar [S/N]: '))
    if c in "Nn":
        break
print(f'Sua lista contém {len(pessoas)} pessoas')
print('Pessoas mais pesadas: ',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p,end=' ')
print('\nPessoas mais leves: ',end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p,end=' ')


