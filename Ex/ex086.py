#crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
print('\033[34m')
matriz = [[],[],[]]
for i in range(0,3):
    for v in range(0,3):
        matriz[i][v].append(int(input('Digite um valor para a matriz: ')))
print(matriz)