# leia 4 valores e guarde em uma tupla
n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),)
# quantas vezes o valor 9 aparece?
print(f'O N. 9 aparece: {n.count(9)}x')
# em que posição foi digitado o primeiro 3
if 3 in n:
    print(f'3 foi o {n.index(3)+1}° numero digitado.')
else:
    print('Nenhum N. 3')
# quais foram os numeros pares
print('Os numeros pares foram: ', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
