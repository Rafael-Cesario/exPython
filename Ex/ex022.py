#leia o nome de uma pessoa -
#transforme todas as letras em maiúsculas - 
#transforme todas em minúsculas - 
#quantas letras ao todo sem contar espaços -
#quantas letras tem o primeiro nome -

nome = str(input('Digite seu nome completo: ')).strip()
print(nome)
print(nome.upper())
print(nome.lower())
print('{} tem: {} Letras'.format(nome, len(nome) - nome.count(' ')))
separarNome = nome.split()
print('{} tem: {} Letras'.format(separarNome[0],len(separarNome[0])))