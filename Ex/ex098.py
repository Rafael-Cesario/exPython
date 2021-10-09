#faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep
def contador(i, f, p):
    if i > f:
        for c in range(i, f-1, -p):
            if c == f:
                print(c)
            else:
                print(f'{c} >> ', end='', flush=True)
                sleep(0.5)
    else:
        for c in range(i, f+1, p):
            if c == f:
                print(c)
            else:
                print(f'{c} >> ',end='', flush=True)
                sleep(0.5)


contador(1,10,1)
contador(10, 0, 2)
print('Faça a sua propria contagem: ')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if c < 0:
    c *= -1 
if c == 0:
    c = 1
contador(a, b, c)