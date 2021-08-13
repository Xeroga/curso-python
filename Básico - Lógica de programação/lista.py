"""
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# indices    0  1  2  3      4       5    6
# lista =     [1, 2, 3, 4, 'xeroga', True, 2.8]
#        -   6  5  4  3      2       1    0

# print(lista[4])
# print(lista[-1])
#
# lista[6] = 'teste'
# print(lista[6])
#
# print(lista[:4])
# print(lista[::-1])  # mostrara de forma invertida

l1 = [1, 2, 3]
l2 = [4, 5, 6]
# l1.extend(l2)  # add o valor da l2
# l1.extend('a')
# l3 = l1 + l2

# print(max(l2))  # mostra o maior valor da lista
# print(min(l2))
#
# l2.append('b')  # insere um novo valor no final da lista
#
# l2.insert(0, 'banana')  # add no indice 0 passando os outros para a frente sem excluir o valor
# # print(l1)
# print(l2)
# print(l2[0])
# print(l2)
#
# l2.pop()  # remove o ultimo valor
# print(l2)
#
# del(l2[1:3])  # deleta o indice
# print(l2)

# l4 = list(range(1, 10))
# print(l4)
#
# soma = 0
# for valor in l4:
#     soma += valor
# print(soma)

# l5 = ['String', True, 10, -20.5]
#
# for elem in l5:
#     print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

#######
secreto = input('Digite um palavra secreta:')
qnt = len(secreto)
digitadas = []
chances = int(qnt // 2)

while True:
    #chances
    if chances <= 0:
        print('Voce perdeu!!')
        break
    print(50*'=')
    print(f' voce tem {chances} chances.')
    print(f'A palavra secreta tem {qnt} letras.')
    letra = input('Digite uma letra: ')
    # verificar se digitou mais de  letra
    if len(letra) > 1:
        print('Isso nao vale')
        continue
    # add na lista oq foi digitado
    digitadas.append(letra)
    # verificar se a letra existe na palavra secreta
    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta.')
    else:
        print(f'A letra {letra} nao existe na palavra secreta.')
        chances -= 1
        digitadas.pop() #  exclui a ultima letra digitada da lista
    # montando a palavra secreta
    secreto_tmp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_tmp += letra_secreta
        else:
            secreto_tmp += '*'
    # verificar se ganhou
    if secreto_tmp == secreto:
        print('Que legal, VOCE GANHOU!!!')
        print(f'A palavra secreta era {secreto}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_tmp}')