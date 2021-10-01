#mostre o maior e o menor entre 5 valores
maior = 0
menor = 0
for v in range(1,6):
    valor = float(input('Digite um valor: '))
    if v == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
