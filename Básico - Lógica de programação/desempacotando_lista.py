"""
Desempacotamento de lista - inicio, *_, final
"""

lista = ['luiz', 'joao', 'maria'] # !add mais um valor para ver

n1, n2, n3 = lista  # variaveis tem que ter a mesma qnt que a lista
print(n2)

lista = ['luiz', 'joao', 'maria', 1, 2, 3, 4, 5, 6]
# n1, n2, n3, *outra_lista = lista  # * pega o restante da lista e coloca em outra lista
n1, n2, n3, *outra_lista, ultimo_da_lista = lista  # pega o ultimo valor da lista
print(n1, n2, outra_lista)
print(ultimo_da_lista)