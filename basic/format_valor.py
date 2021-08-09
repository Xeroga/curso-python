"""
:s  -Texto (str)
:d  -Inteiro (int)
:f  -Num Flutuante(float)
:.(num)f    -Qnt de casas decimais (float)    ex: :.2f
:(caractere)(> OU < ^)(qnt)(tipo - s, d ou f)  ex: :0>10

> - esquerda
< - direita
^ - centro
"""

num1 = 1
print(f'{num1:0>10.2f}')

num2 = 2
print(f'{num2:0<10}')

title = 'Login'
print(f'{title:-^25s}')

title_format = input('Digite um titulo: ')
title_format = title_format.upper() # tudo maiusculo
#  title_format = title_format.lower() # tudo minusculo
#  title_format = title_format.title() # primeiras letras maiusculas

title_format = '{t:=^25s}'.format(t=title_format)  # somara o titulo com = ate ter 25 caracteres


print(title_format)
print(len(title_format))