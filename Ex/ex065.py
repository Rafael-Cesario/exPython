#ler uma quantidade indeterminada de numeros e dizer o maior, menor, média, soma, quantidade de valores
parar = 'N'
media = soma = quanti = menor = maior = 0
while parar != 'S':
    n = int(input('Digite um numero: '))
    parar = str(input('Quer parar [S/N]: ')).upper().strip()[0]
    quanti += 1
    soma += n
    if quanti == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / quanti
print('\nQuantidade de valores: {}'.format(quanti))
print('Soma entre eles: {}'.format(soma))
print('Média: {:.2f}'.format(media))
print('O maior valor lido foi: {}'.format(maior))
print('O menor valor lido foi: {}'.format(menor))
print('FIM\n')