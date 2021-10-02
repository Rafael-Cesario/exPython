#utilizando flag break
quanti = soma = 0
n = int(input('Digite um numero: '))
while True:
    quanti += 1
    soma += n
    n = int(input('Digite um numero: '))
    if n == 999:
        break
print(f'Numeros digitados: {quanti}\nSoma entre eles = {soma}')