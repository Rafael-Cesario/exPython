#Analisando e gerando Dicionários
def notas(*notas, sit=False):
    """ Calcula o total de notas passadas, a maior nota, a menor, a média e caso {sit} esteja em true, mostra a situação em que o aluno se encontra.
    :parm notas: notas
    :parm sit: valor booleano use sit=True/False"""
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = f'{sum(notas) / total:.1f}'
    resp = {
        "Total": total,
        "Maior": maior,
        "Menor": menor,
        "Média": media,}
    if sit:
        if float(media) < 3:
            resp["Situação"] = "Ruim"
        elif float(media) < 6:
            resp["Situação"] = "Recuperação"
        elif float(media) < 9:
            resp["Situação"] = "Bom"
        elif float(media) == 10:
            resp["Situação"] = "Otimo"
    return resp


resp = notas(10,10,10,5 , sit=True)
print(resp)
help(notas)