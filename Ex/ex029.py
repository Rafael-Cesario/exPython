# leia a velocidade de um carro
# if > 80km == multado
# para cada km acima do limite +R$7,00
cores = {
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'branco': '\033[7m',
    'reset': '\033[m',
}
vel = int(input('Digite a velocidade do carro: '))
print('Sua velocidade é: {}km/h'.format(vel))
if vel > 80:
    print(cores['vermelho'], 'Você esta acima do limite de velocidade e foi multado em R${}'.format(
        (vel - 80) * 7))
else:
    print(cores['verde'], 'Boa viagem')
    print(cores['verde'], 'Dirija com cuidado :)')
