#leia o primeiro termo e razão PA, mostre os 10 primeiros termos
termo = int(input('Termo: '))
razao = int(input('Razão: '))
q = 0
while q != 10:
    print(termo, end=' ')
    termo += razao
    q += 1
    