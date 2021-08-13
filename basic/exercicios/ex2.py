# obter dados
nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
altura = input('Qual a sua altura: ')
peso = input('Qual o seu peso: ')
# converte
idade = int(idade)
altura = float(altura)
peso = float(peso)
# inicio
ano = 2021
an = ano -idade
imc = peso / altura ** 2
# resultado
print(50*"-")
print(f'{nome} nasceu em {an}, seu IMC e {imc:.2f}')