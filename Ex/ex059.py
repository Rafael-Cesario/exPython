#criando um menu
from time import sleep
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
option = 0
while option != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa
    ''')
    option = int(input('Digite sua opção: '))
    if option == 1:
        soma = v1 + v2
        print('{} + {} = {}'.format(v1, v2, soma))
    elif option == 2:
        m = v1 * v2
        print('{} . {} = {}'.format(v1, v2, m))
    elif option == 3:
        if v1 > v2:
            print('{} é o maior'.format(v1))
        else:
            print('{} é o maior'.format(v2))
    elif option == 4:
        v1 = int(input('Valor 1: '))
        v2 = int(input('Valor 2: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção invalida')
    print('\033[34m-='*20,'\033[m')
    sleep(1)