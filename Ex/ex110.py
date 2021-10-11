#Criando Modulos
#melhor o ex107 criando um função dentro de um modula para formatar moedas
#melhore o ex108
#melhore o ex109
from Modulos import moeda, estilo

estilo.letra("Azul")
valor = float(input('Valor: '))
porcentagem = float(input('porcentagem: '))


moeda.resumo(valor, porcentagem, "Amarelo")
estilo.letra("Default")