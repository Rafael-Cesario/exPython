#Mostre os 10 primeiros valores de uma PA
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
décimo = termo + (10 - 1) * razao
for c in range(termo, décimo + razao, razao):
    print('{} »'.format(c,), end=' ')
print('ACABOU')