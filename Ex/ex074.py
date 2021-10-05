#trupla com numeros aleatorios,
#numeros na tupla
from random import randint
ns = (randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20))
print('Entre os numeros: ',  end=' ')
for n in ns:
    print(n,  end=' ')
#maior e o menor
print(f'''\n
O menor numero é: {min(ns)}
E o maior é: {max(ns)}\n''')