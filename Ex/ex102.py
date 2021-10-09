#calcule o fatorial de um numero com a opção de mostrar o processo de fatoração ou não
def fato(v,show=False):
    """
    >>> Calcula o fatorial de um numero:
    :param v: O numero a ser calculado
    :param show: (opcional) Diz se a conta deve ser mostrada ou não.
    """
    if show == True:
        print(f'{v}! = {v}', end='')
        for c in range(v-1,0,-1):
            print(f'.{c}', end='')
            v *= c
        print(f' = {v}')
    else:
        for c in range(v-1,0,-1):
            v *= c
        return v


print('\033[34m')
fatorial = int(input('Fatore: '))
processo = str(input('Mostrar processo [S/N]: ')).strip().upper()
if processo in "S":
    v = fato(fatorial,True)
else:
    v= fato(fatorial)
    print(f'{fatorial}! = {v}')
help(fato)
