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
            v1 = int(input(f'{estilos.letra(txt, "Azul")}'))
        except ValueError:
            print(estilos.letra("Valor digitado não é valido", "Vermelho"))
        else:
            return v1


def leiaFloat(txt):
    while True:
        try:
            v1 = float(input(estilos.letra(txt, "Verde")).strip().replace(",", "."))
        except Exception as error:
            print(estilos.letra("Valor digitado não é valido", "Vermelho"))
        else:
            return v1
