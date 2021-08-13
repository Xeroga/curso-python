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