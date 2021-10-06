print('\033[34m')
#leia 5 valores e guarde em uma lista:
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
#mostre qual o maior e o menor e suas posições na lista
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Entre os valores: {valores}')
print(f'O maior é: {maior}', end=' ')
for i,v in enumerate(valores):
    if valores[i] == maior:
        print(f'na {i} posição', end=' ')
print(f'\nO menor é: {menor}', end=' ')
for i,v in enumerate(valores):
    if valores[i] == menor:
        print(f'na {i} posição', end=' ')
print('\033[m')
