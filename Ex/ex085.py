#criar uma unica lista com valores pares e impares separados em uma lista dentro desta lista
print('\033[34m')
valores = [[],[]]
for c in range(0,7):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
print(f'Valores pares: {sorted(valores[0])}')
print(f'Valores impares: {sorted(valores[1])}')

