"""
Toda função recebe um valor e retorna um valor
Cria uma funcao - def nome(valor):
"""
def funcao():
    print("Ola Mundo!")
funcao()    # chama a funcao

def funcao2(msg='Hello'):
    print(msg)
funcao2('Função 2')

def saudacao(msg, nome):
    nome = nome.replace('e', '3')       # Troca uma letra por outra
    print(msg, nome)

saudacao('Oi', 'Xeroga')    # tem que enviar os valores na ordem

def funcao3(msg='Ola', nome='usuario'):     # Definido um valor padrao
    print(msg, nome)

funcao3(nome='adriano')     # nao pricisa mais ser enviado na ordem

def funcao4():
    msg = 'teste de retorno'
    nome = 'xerogamim'
    return f'{msg} nome: {nome}'    # retorna o valor

variavel = funcao4()

print(variavel)