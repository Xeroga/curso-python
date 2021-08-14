"""
variaveis globais
variaveis locais
funcao pode acessar variaveis de fora
"""
variavel = 'valor'

def func():
    print(variavel)

def func2():
    #global variavel                # usar variavel global nao é uma boa prática de programação
    variavel = 'Outro valor'
    print(variavel)

def func3():    # vai dar erro
    print(variavel)  # vai dar erro pq ela ainda nao foi definida
    variavel = 123  # nao posso setar uma variável local com o msm nome de uma variável global
    print(variavel)

def func4():
    outra_variavel = 'outra'

def func5():  # vai dar erro
    print(outra_variavel)  # nao posso acesar o valor de uma variavel de outra funcao sem o retun


def certo(arg=None):
    arg = arg.replace('v', 'c')  # vai trocar um carácter por outro
    return arg

func()
func2()
func3()
func5()
nova_variavel = certo(arg=variavel)
print(variavel)
print(nova_variavel)
