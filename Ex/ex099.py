#faça uma função maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
    if len(num) > 0:
        print('\033[34mAnalisando os valores...')
        sleep(0.5)
        print(f'{len(num)} valores foram passados: {num}')
        print(f'O maior valor é: {max(num)}\033[m')
        print('-'*20)
    else:
        print('\033[34m0 valores foram passados')
        print('\033[m')



maior(1, 2)
maior(1, 7, 0, 4, 3, 6, 2, 2)
maior(1, 7, 3, 6, 2)
maior()

