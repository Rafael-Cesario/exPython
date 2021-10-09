#Mostre a ficha de um jogador
def ficha(nome="<Desconhecido>", gols=0):
    print(f'\033[34mO jogador {nome} marcou {gols} gols')

a = str(input('Nome: ')).capitalize()
b = str(input('Gols: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(gols=b)
else:
    ficha(a,b)
