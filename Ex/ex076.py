#uma tupla com nome de varios produtos e seus preços:
produtos = ('Celular', 1200, 
            'Abajur', 60, 
            'Monitor', 800, 
            'Controle', 200, 
            'Teclado', 300)
print('\033[34m')
print(f'{"LISTA DE PRODUTOS":^40}')
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<30}', end=' ')
    if p % 2 == 1:
        print(f'R$ {produtos[p]:>7.2f}')
print('\033[m')

