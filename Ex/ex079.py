#cadastre varios valores em uma lista
print('\033[34m')
valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n in valores:
        print('Este numero já foi adicionado')
    else:
        valores.append(n)
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print(f'Valores na sua lsita: {sorted(valores)}')
