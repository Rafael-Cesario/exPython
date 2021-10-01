#ler uma quantidade indeterminada de numeros e somar
n = c = s = 0
n = int(input('Digite um número [999 Stop]: '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número [999 Stop]: '))
print('Digitos: {}'.format(c))
print('Soma: {}'.format(s))
print('FIM\n')