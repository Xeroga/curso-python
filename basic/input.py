"""
Entrada de dados
"""
ano = int(input('Em que ano estamos: '))  # "Type cast" variavel ja vem convertida em inteiro
nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
an = ano - int(idade)
print(50*'-')
print(f'Seu nome e {nome} e voce tem {idade} anos')
print(f'Nasceu em {an}.')
print('Nasceu em', an)