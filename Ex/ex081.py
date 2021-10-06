#leia varios numeros e coloque eles em uma lista:
from typing import Counter


print('\033[34m')
numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        c = str(input('Continuar [S/N]: ')).strip().upper()
        if c in "SN":
            break
    if c in "N":
        break
print(numeros)
#quantos numeros foram digitados:
print(f'{len(numeros)} numeros foram digitados')
#lista em ordem decrecente:
print(f'Valores em ordem decrecente: {sorted(numeros, reverse=True)}')
#verificar o valor 5:
if 5 in numeros:
    c = numeros.count(5)
    print(f'Encontrei {c} cinco')
else:
    print('Nâo encontrei nenhum numero 5')
