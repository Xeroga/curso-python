"""
Enquanto condicao for verdadeira
"""
"""
while True:  # enquanto -- loop infinito
    nome = input('Qual o seu nome: ')
    print(f'Ola {nome}!')
"""

x = 1
while x < 10: # no caso vai mostrar so 9
    print(x)
    x = x + 1
print('Acabou!')

# Exemplo 2
x = 1
while x < 10: # no caso vai mostrar so 9
    if x == 3:
        print(f'"{x} sera pulado."')
        x = x + 1
        continue  # pula um laco de repeticao
    print(x)
    x = x + 1
print('Acabou!')

# Exemplo 3
x = 1
while x < 10: # no caso vai mostrar so 9
    if x == 5:
        x = x + 1
        break  # finaliza laco de repeticao
    print(x)
    x = x + 1
print('Acabou!')

# Exemplo 4
x = 0  # coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1  # y = y + 1
    x += 1
print('Acabou!')

# Exemplo 5

while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    op = input('Digite um operador: ')  #  + - * /
    sair = input('Deseja sair? [s]im ou [n]ao: ')

    if sair == 's':
        break

#  verifica se nao e numero
    if not n1.isnumeric() or not n2.isnumeric():
        print('Voce precisa digitar um numero.')
        continue # se nao for vai pular

    n1 = int(n1)
    n2 = int(n2)

    if op =='+':
        print(n1+n2)
    elif op =='-':
        print(n1-n2)
    elif op =='*':
        print(n1*n2)
    elif op =='/':
        print(n1/n2)
    else:
        print('Operador invalido!')