from pacotes import estilos, interface


def arqExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(estilos.letra("Houve um ERRO ao criar o arquivo", "Vermelho"))
    else:
        print(estilos.letra(f"Arquivo criado com sucesso: {nome}", "Verde"))


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print(estilos.letra("Erro ao ler o arquivo" , "Vermelho"))
    else:
        interface.titulo("Pessoas Cadastradas", "Amarelo")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(estilos.letra(f'{dado[0]:<30}\t{dado[1]:>3} Anos', "Verde"))
    finally:
        a.close()

def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print(estilos.letra("Erro ao abrir o arquivo" , "Vermelho"))
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(estilos.letra("Erro ao escrever no arquivo", "Vermelho"))
        else:
            print(estilos.letra('Nova pessoa adicionada', 'Verde'))
            a.close()