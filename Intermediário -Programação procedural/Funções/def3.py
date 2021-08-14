"""
    *args **kwargs
"""
# depois que difinir uma argumento os outros tem que sequir o msm padrao
def func(a1, a2, nome=None): # Ex.: a1, a2, nome=None, a3=None
    #print(a1, a2, nome)
    return nome, a1  # retornara uma tuple

var = func(1,2,nome='xeroga')  # aqui tem q sequir o msm padrao da funcao
print(var)
print(var[0], var[1])  # acessa o índice da tuple retornada

print()
print(f'{" DESEMPACOTANDO ":=^25}')  # --------------------------
print()

lista = [1, 2, 3, 4, 5]
print(lista)  # lista normal
n1, n2, *n = lista  # desempacotando a lista
print(n1, n2, n)
# desempacotando toda a lista
print(*lista)  # retorna uma tuple(lista nao editável)

print()
print(f'{" CONVESÃO ":=^25}')  # --------------------------
print()

def func2(*args):
    args = list(args)  # convertendo tuple para lista
    args[0] = 20
    print(args)
    # print(args[0])
    # print(args[-1])
    # print(len(args))
func2(1, 2, 3, 4, 5)

print()
print(f'{" SOLUÇÃO *args ":=^25}')  # --------------------------
print()

def sol(*args):
    print(args)

lista = [1, 2, 3, 4, 5, 6]
lista2 = [40, 50, 60]
sol(*lista, 10, 20, 30)  # enviar uma lista descompactada
sol(*lista, *lista2)

print()
print(f'{" SOLUÇÃO *kwargs ":=^25}')  # --------------------------
print()

def sol(*args, **kwargs): # argumentos com palavras chave
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['snome'])  # se variavel nao estiver definida vai da erro
    # verifica se foi passado arg idade
    idade =kwargs.get('idade')
    print(idade)  # mostrara None se nao estiver definida

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')

lista = [1, 2, 3, 4, 5, 6]
lista2 = [40, 50, 60]

sol(*lista, *lista2, nome='rubens', snome='adriano')