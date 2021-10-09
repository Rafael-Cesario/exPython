#faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda funçã ovai mostar a soma entre todos os valores pares sorteados pela função a anterior.
from random import randint
def sorteia(n):
    for c in range(0, 5):
        n.append(randint(0, 10))
    print(f'Numeros sorteados: {numeros}')
def somaPar(ns):
    s = 0
    for n in ns:
        if n % 2 == 0:
            s += n
    print(f'Soma apenas dos valores pares: {s}')


print('\033[34m')
numeros = list()
sorteia(numeros)
somaPar(numeros)