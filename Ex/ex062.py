#Contador PA
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total :
        print(termo, end = ' ')
        termo += razão
        c += 1
    mais = int(input(('\nQuer mostrar mais quantos termos: ')))
print('Finalizado com {} termos'.format(c))


