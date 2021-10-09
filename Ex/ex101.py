#retorne se uma pessoa tem voto , negado, opcional, ou obrigatorio
def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade >= 16 and idade < 18 or idade >= 70:
        return str('Opcional')
    elif idade >= 18:
        return str('Obrigatório')
    else:
        return str('Negado')


print('\033[34m')
nome = str(input('Nome: ')).capitalize()
nasc = int(input('Ano de nascimento: '))
teste = voto(nasc)
print(f'{nome} seu voto é {teste}')