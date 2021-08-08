idade = input("Qual a sua idade: ")
idade = int(idade)  # convert str to int
# verificacao
if idade < 18:
    print('Menor de idade.')
else:
    print('Maior de idade.')