nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

if idade >= 18 and idade < 30:
    print(f'{nome} pode pegar o imprestimo.')
else:
    print(f'{nome} nao pode pegar o imprestimo.')