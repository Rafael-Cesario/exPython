#verificar se existe silva no nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem silva: {}'.format('silva' in nome.lower()))
