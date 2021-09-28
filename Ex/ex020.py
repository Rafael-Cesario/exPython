#embaralhe a ordem inserida
from random import shuffle
n1 = input('Primeiro digito: ')
n2 = input('Segundo digito: ')
n3 = input ('Terceiro digito: ')
n4 = input ('Quarto digito: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem é: {}'.format(lista))