#Criando um menu, utilizando arquivos
from pacotes import interface, estilos, arquivo


arq = "Ex-115.txt"

if not arquivo.arqExiste(arq):
    arquivo.criarArquivo(arq)

interface.titulo("Sistema v1.0", "Amarelo")
while True:
    user = interface.menu(["Ver pessoas cadastradas", "Cadastrar Pessoas", "Sair do Sistema"])
    if user == 1:
        arquivo.lerArquivo(arq)
    elif user == 2:
        interface.titulo("Cadastrar Pessoas", "Amarelo")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        arquivo.cadastrar(arq, nome, idade)
    elif user == 3:
        interface.titulo("Saindo do sistema..." , "Amarelo")
        break
    elif user > 3 or user < 1:
        print(estilos.letra('opção invalida', "Vermelho"))
