"""
str indices
fatiamento de str [inicio:fim:passo]
Funcao build-in len, abs, type, print, etc...
"""
#  positivos [012345678]
nome    =    'Python s2'
# negativos -[987654321]
print(nome[2])

url = 'www.google.com.br/'

#print(url[:-1])
print(url[0::3])  # pular ::
#  fatiando str
nova_str = nome[2:6]  # o fim nao é incluido
print(nova_str)
print(len(nome))

# exemplo
for letra in nome:
    print(letra)