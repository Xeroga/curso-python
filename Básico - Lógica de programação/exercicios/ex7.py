nome = input('Qual o seu nome: ')

qnt = len(nome)

if qnt <= 4:
    print('Seu nome e curto')
elif qnt >= 5 and qnt <= 6:
    print('Seu nome e normal')
else:
    print('Seu nome e muito grande')