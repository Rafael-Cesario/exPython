#tratamento de erros
from pacotes import dados,estilos
v1 = dados.leiaInt("Digite um valor inteiro: ")
v2 = dados.leiaFloat("Digite um numero real: ")

print(estilos.letra(f'Valor Inteiro: \t{v1}\nValor Real: \t{v2}', "Amarelo"))