#Seletor
pessoas = 0
idadeMedia = 0
velho = ['', 0]
menorde20 = 0
for p in range(0,4):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    print('-='*20)
    pessoas += 1
    idadeMedia += idade
    if sexo == 'm':
        if idade > velho[1]:
            velho = [nome, idade]
    if sexo == 'f':
        if idade < 20:
            menorde20 += 1
        
        
idadeMedia = idadeMedia / pessoas
print('A média de idade do grupo é {:.0f}'.format(idadeMedia))
print('O Homem mais velho é {} e ele tem {}'.format(velho[0], velho[1]))
print('Há {} mulheres menores de 20'.format(menorde20))


