from pacotes import estilos


def leiaDinheiro():
    while True:
        v = str(input("Valor: R$ ")).replace(",", ".").strip()
        if v.isalpha() or v == "":
            estilos.letra("Vermelho")
            print(f'\"{v}\" não é um valor valido')
            estilos.letra("Azul")
        else:
            break
    return float(v)


def leiaInt(txt):
    while True:
        try:
            v1 = int(input(f'{estilos.letra("Azul")}{txt}{estilos.letra("Default")}'))
        except ValueError:
            print(f"{estilos.letra('Vermelho')}Valor digitado não é valido.{estilos.letra('Default')}")
        else:
            return v1
