#Testar se um site esta acessivel
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'\033[31mO site esta fora do ar')
else:
    print(f'\033[32mO site esta acessivel')