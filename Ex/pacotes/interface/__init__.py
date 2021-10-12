from pacotes import estilos,dados

def linha(tam=42,cor="Default"):
    print(estilos.letra("-"*tam, cor),)


def titulo(txt,cor):
    linha(cor=cor)
    print(estilos.letra(txt.center(42), cor))
    linha(cor=cor)


def menu(lista):
    titulo("Menu" , "Azul")
    c = 1
    for item in lista:
        print(estilos.letra(f'{c} - {item}',"Azul"))
        c += 1
    linha(cor="Azul")
    user = dados.leiaInt("Opção: ")
    return user
    
