#compare dois numeros inteiros, mostrando qual valor é maior ou se eles são iguais
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
if v1 > v2:
    print('{} é maior'.format(v1))
elif v2 > v1:
    print('{} é o maior'.format(v2))
else:
    print('os dois valores são iguais')