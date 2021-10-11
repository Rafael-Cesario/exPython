from pacotes import estilos


def aumentar(v=0, p=0, f=False):
    res = v + (v * p / 100)
    return res if f is False else moeda(res)


def diminuir(v=0, p=0, f=False):
    res =  v - (v * p /100)
    return res if f is False else moeda(res)


def dobro(v=0, f=False):
    res = v * 2
    return res if f is False else moeda(res)


def metade(v=0, f=False):
    res = v / 2
    return res if f is False else moeda(res)


def moeda(v=0, f="R$"):
    res = f'{f}{v:.2f}'.replace(".", ",")
    return res


def resumo(v=0, p=0, c="Default"):
    estilos.letra(c)
    print('-'*20)
    print('RESUMO'.center(20))
    print('-'*20)    
    print(f'A metade de {moeda(v)} é : \t{metade(v, True)}')
    print(f'O dobro de {moeda(v)} é:  \t{dobro(v, True)}')
    print(f'Aumentando {p}% de {moeda(v)}: \t{aumentar(v, p, True)}')
    print(f'Diminuindo {p}% de {moeda(v)}: \t{diminuir(v, p, True)}')

