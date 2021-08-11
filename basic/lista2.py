secreto = 'python'
resposta = ''
digitadas = ['t', 'h', 'o', 'p', 'y']

for letra_secreto in secreto:
    print(f'Iteracao para letra {letra_secreto}')

    if letra_secreto in digitadas:
        print(f'A letra que eu queria {letra_secreto}')
        resposta += letra_secreto
    else:
        resposta += '*'
print()
print(resposta)

if secreto ==resposta:
    print('Voce Ganhou!')