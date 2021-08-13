nome = 'xeroga'
idade = 25
peso = 64
altura = 1.75
e_maior = idade >= 18
imc = peso / altura ** 2
# inicio
print('Nome:', nome)
print('E maior:', e_maior)
print('IMC:', imc)
# format string
print(f'{nome} tem {idade} anos de idade e seu imc e {imc}')
#                                                   mostrara 2 casa depopis do .
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')
#                                                    ordem 0     1       2
print('{0}, {1} tem {1} anos e seu imc e {2:.2f}'.format(nome, idade, imc))
# renomear as variaveis
print('{n} tem {i} anos e seu imc e {im:.2f}'.format(n=nome, i=idade, im=imc))