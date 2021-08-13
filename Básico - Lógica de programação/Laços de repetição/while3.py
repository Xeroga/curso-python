"""
Iterar um elemento
"""
#        Índice
#        0123456789......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

#  print(tamanho_frase)
# print(frase[5])

# while contador < 10:
#     print(frase[contador], contador)
#     contador += 1

nova_str = ''

# while contador < tamanho_frase:
#     #  print(frase[contador], contador)
#     nova_str += frase[contador]
#     contador += 1
#     print(nova_str)

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_str += 'R'  # .upper() deixa letra maiúscula
    else:
        nova_str += letra
    contador += 1
print(nova_str)