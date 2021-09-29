#par ou impar
n = int(input('Digite um numero: '))
nn = n % 2
if nn > 0:
    print('{} é impar'.format(n))
else:
    print('{} é par'.format(n))