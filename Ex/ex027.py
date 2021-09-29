#leia o nome completo de uma pessoa e mostre separadamente o primeiro e o ultimo nome
nome = str(input('Digite o seu nome aqui: ')).strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))

