#criar uma unica lista com valores pares e impares separados em uma lista dentro desta lista
valores = [[],[]]
for c in range(0,7):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
print(f'Entre os valores: {valores}')
print(f'Valores pares: {valores[0]}')
print(f'Valores impares: {valores[1]}')

