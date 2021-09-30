# Leia um número e diga se ele é primo
num = int(input('Digite um numero: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if total > 2:
    print('\nEle não é primo')
else:
    print('\nPRIMO')
    