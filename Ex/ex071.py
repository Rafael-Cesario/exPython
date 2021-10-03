#simulando um caixa eletronico utilizando notas de R$50,20,10,1
print(f'\033[32m-='*20)
print('{:^40}'.format('BANCO'))
print(f'-='*20,'\033[m')
valor = int(input('Quanto você gostaria de sacar? R$ '))
dinheiro = 50
dintotal = 0
while True:
    if dinheiro <= valor:
        valor -= dinheiro
        dintotal += 1
    else:
        if dintotal > 0:
            print(f'\033[32m{dintotal} notas de {dinheiro}\033[m')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 10:
            dinheiro = 1
        dintotal = 0
        if valor == 0:
            break



