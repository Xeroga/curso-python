def funcao(var):
    print(var)
    # quando nao define o return ele volta um valor None
    return var
variavel = funcao('Valor que eu quero')     # envia e recebe os valores da funcao

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')
# -------------------------------------------------
def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divide = divisao(8,0)
if divide:
    print(divide)
else:
    print('Conta invalida.')

# -----------------------------------------------
# retorna um funcao dentro da outra
def f(var):
    print(var)
def dump():
    return f

var = dump()
# var passa a ser uma funcao agora
var('Pode imprimir algo na tela.')
print(id(var), id(f)) # mostra o id na memoria

if var == f:
    print('var é igual a f')
else:
    print('blaaaaaa')

print(25*'-')
# tuples é uma lista que não pode ser alterada
def tuple():
    return ('rubens', 'adriano')
lista = tuple()

print(lista, type(lista))