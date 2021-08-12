"""
OR - verifica se a variavel esta vazia
"""

nome = input('Qual o seu nome: ')
print(nome or 'Voce nao digitou nada!') # OR pega o valor verdadeiro

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print(variavel)