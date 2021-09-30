#verifique se uma frase é palíndromo.
frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
for c in range(len(juntar)-1, -1, -1):
    inverso += juntar[c]
print('A frase {} ao contrario é {}'.format(juntar, inverso))
if inverso == juntar:
    print('Sua frase é um palíndromo')
else:
    print('Sua frase não é um palíndromo')