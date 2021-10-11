#Criando Modulos
#melhor o ex107 criando um função dentro de um modula para formatar moedas
#melhore o ex108
from Modulos import moeda, cor

cor.letra("Azul")
valor = float(input('Valor: '))
porcentagem = float(input('porcentagem: '))


cor.letra("Amarelo")
print(f'A metade de {moeda.moeda(valor)} é : {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor, True)}')
print(f'Aumentando %{porcentagem} de {moeda.moeda(valor)}: {moeda.aumentar(valor, porcentagem, True)}')
print(f'Diminuindo %{porcentagem} de {moeda.moeda(valor)}: {moeda.diminuir(valor, porcentagem, True)}')
cor.letra("Default")