# tupla, preencha com 20 primeiros colocados da tabela do brasileirão
times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino',
         'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR', 'Atlético-GO', 'Cuiabá', 'Ceará', 'São Paulo', 'América-MG', 'Juventude', 'Santos', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
print(f'\n\033[32mOs 5 primeiros colocados na tabela são:\n{times[:5]}')
print(f'\nOs últimos 4 colocados são: \n{times[-1:15:-1]}')
print(f'\nTimes em ordem alfabética: \n{sorted(times)}')
print(f'\nChapecoense está na {times.index("Chapecoense")+1}° posição\033[m')
