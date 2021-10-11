#Criando Modulos
#melhore o ex107 criando um função dentro de um modula para formatar moedas
from Modulos.moeda import metade
from Modulos import moeda, cor

cor.letra("Azul")
valor = float(input('Valor: '))
porcentagem = float(input('porcentagem: '))


cor.letra("Amarelo")
print(f'A metade de {moeda.moeda(valor)} é : {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando %{porcentagem} de {moeda.moeda(valor)}: {moeda.moeda(moeda.aumentar(valor, porcentagem))}')
print(f'Diminuindo %{porcentagem} de {moeda.moeda(valor)}: {moeda.moeda(moeda.diminuir(valor, porcentagem))}')
cor.letra("Default")