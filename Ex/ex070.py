# Leia o nome e preço de varios produtos,mostre total gasto, quantos produtos custão mais de 1000, qual é o nome do produto mais barato
total = mil = quantidade = 0
while True:
    produto = str(input('Produto: ')).strip()
    preço = float(input('Preço: R$ '))
    quantidade += 1
    if quantidade == 1 or preço < barato[0]:
        barato = [preço, produto]
    if preço > 1000:
        mil += 1
    total += preço
    while True:
        continua = str(input('Adicionar outro [S/N]: ')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua in 'N':
        break
print(f'\033[32mTotal compra: R$ {total}')
print(f'{mil} produtos custam mais de R$ 1000')
print(f'{barato[1]} é o produto mais barato custando {barato[0]}\033[m')
print('\nFIM')
