#leia uma frase e mostre
#quantas vezes a letra "a" aparece
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez
frase = str(input('Digite uma frase = ')).upper().strip()
print('A letra "A" aparece: {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição: {}'.format(frase.rfind('A')+1))