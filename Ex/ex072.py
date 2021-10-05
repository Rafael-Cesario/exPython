#crie uma tupla que tenha uma contagem por extenso do zero ao vinte
extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input('\nDigite um valor de 0 a 20: '))
    if valor >= 0 and valor <= 20:
        break
print(f'{valor} em extenso é: {extenso[valor].capitalize()}\n')