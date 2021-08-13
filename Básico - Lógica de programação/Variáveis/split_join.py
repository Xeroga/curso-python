"""
Split, Join, Enumerate
* Split - Divide um string # str
* Join - Junta uma lista # str
* Enumerate - Enumera elementos da lista # iteraveis
"""
# frase = "O brasil é uma merda, brasil país lixo."
# l1 = frase.split(' ')  # separa a lista com spaço
# l2 = frase.split(',')
#
# print(l1)
# print(l2)

# for valor in l2:
#     print(valor.strip())  #  tira o espaço do começo e final de uma frase

# palavra = ''
# contagem = 0
# for valor in l1:
#     #  print(f'A palavra {valor} apareceu {l1.count(valor)}x na frase')
#     qnt_vezes = l1.count(valor)
#     if qnt_vezes > contagem:
#         contagem = qnt_vezes
#         palavra = valor
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}X)')

# brasil = 'o brasil é penta'
# lista_nova = '*'.join(brasil)  # juntou brasil com *
# print(lista_nova)

# lista_nova = brasil.split(' ')
#
# for indice, valor in enumerate(lista_nova):
#     print(indice, valor)


#  uma lista dentro de outra
lista = [
    [0, 'Luiz'],
    [1, 'joao'],
    [2, 'maria'],
]

for indice, valor in lista:
    print(indice, valor)
#  -----------------------------------
lista2 = ['Luiz', 'joao', 'maria']
n1, n2, n3 = lista2  # desempacotando a lista
print(n2)
for indice, valor in enumerate(lista2):
    print(indice, valor)
