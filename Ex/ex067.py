#tabuada
tabuada = int(input('\nQuer ver a tabuada de qual numero? '))
while True:
    c = 1
    print(f'\ntabuada do {tabuada}')
    while c <= 10:
        total = tabuada * c
        print(f'{tabuada:2} . {c:2} = {total}')
        c +=1
    tabuada = int(input('\nQuer ver a tabuada de qual numero? '))
    if tabuada < 0:
        break
