#leia varios numeros e coloque em uma lista:
print('\033[34m')
numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        c = str(input('Continuar [S/N]: '))
        if c in "SsNn":
            break
    if c in "Nn":
        break
#cria listas apenas para os pares e outra para impares
pares = []
impares = []
for i,v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
#mostre as três listas
print(f'Todos os valores: {numeros}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')