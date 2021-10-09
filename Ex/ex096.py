#faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular ( largura e comprimento) e mostre a área do terreno.
def l1():
    print('\033[34m-='*26)
def l2():
    print('-='*26, '\033[m')
def area(a,b):
    s = a * b
    print(f'Area: {s}m²')


l1()
a = float(input('Largura: '))
b = float(input('Comprimento: '))
area(a,b)
l2()