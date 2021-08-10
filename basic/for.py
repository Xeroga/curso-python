"""
For in Python
Iterando strings com for
Funcao range(start=0, stop, step=1)
"""

texto = 'Python'
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# for letra in texto:
#     print(letra)

# for n in range(10):  # range gera numero
#     print(n)

# for n in range(20, 10, -1):  # stop nao incluso
#     print(n)
#
# print(25*'-')
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

# continue - pula para o proximo laco
# break - termina o laco
nova_str = ''
for letra in texto:
    if letra == 't':
        continue  # vai pular o 't'
        nova_str += letra.upper()
    elif letra == 'h':
        nova_str += letra.upper()
        break  # finaliza o laço
    else:
        nova_str += letra
print(nova_str)