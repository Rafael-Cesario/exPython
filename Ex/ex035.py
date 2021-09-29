# leia o comprimento de três retas. Diga ao usuario se elas podem formar um triângulo
cores = {
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'branco': '\033[7m',
    'reset': '\033[m',
}
reta1 = float(input('Digite o valor da reta1: '))
reta2 = float(input('Digite o valor da reta2: '))
reta3 = float(input('Digite o valor da reta3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(cores['azul'], 'Suas retas podem formar um triângulo')
else:
    print(cores['vermelho'], 'Suas retas não podem formar um triângulo')
