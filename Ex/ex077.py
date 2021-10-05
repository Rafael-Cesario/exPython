#uma tupla com varias palavras, ache as vogais de cada palavra:
palavras = ('Estas', 'Sao', 'teste', 'palavras', 'arroz', 'controle', 'monitor', 'camera', 'abajur', 'rafael', 'eu', 'pessoa',)
print('\033[34m')
for p in palavras:
    print(f'\nVogais na palvra {p.upper()} = ', end=' ')
    for v in p.upper():
        if v in 'AEIOU':
            print(v, end=' ')
print('\033[m')