#somando apenas os pares
soma = 0
for valor in range(0, 6):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        soma += valor
print('A soma entre os valores pares é {}'.format(soma))


    
    