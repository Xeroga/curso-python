"""
Enumerate - Enumerar elementos da lista # list
"""

lista = [
    #   0      1      2
    ['edu', 'jao', 'luiz'], # 0
    ['maria', 'aline', 'joana'], # 1
    ['helena', 'ed', 'lu'], # 2
]

print(lista[2])
print(lista[1][2])

# enumerada = enumerate(lista)
# print(list(enumerada))
enumerada = enumerate(lista)
print(list(enumerada))


print(50*'=')

for v1, v2 in enumerate(lista, 53):  # aqui voce vai entender
    print(v1, v2)

print(50*'=')


for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    print(minha_lista)
    # nome1, nome2, nome3 = minha_lista
    # print(nome1, nome2, nome3)