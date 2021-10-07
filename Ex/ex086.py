#crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
print('\033[34m')
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite uma valor para {[l,c]}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
        