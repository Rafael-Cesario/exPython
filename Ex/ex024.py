#verificar a primeira palavra de uma frase
cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].lower() == 'santo')
