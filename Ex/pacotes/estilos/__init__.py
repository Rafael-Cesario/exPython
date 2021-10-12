def letra(txt="None", cor='Default'):
    c = valores[cor]
    return (f'{c}{txt}{valores["Default"]}')

valores = {
    'Default': '\033[m',
    'Vermelho': '\033[31m',
    'Verde': '\033[32m',
    'Amarelo': '\033[33m',
    'Azul': '\033[34m',
    'Inverter': '\033[;7m',
}
