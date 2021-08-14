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
print(f'{" SOLUÇÃO ":=^25}')  # --------------------------
print()

def sol(*args):
    print(args)

lista = [1, 2, 3, 4, 5, 6]
sol(*lista, 10, 20, 30)  # enviar uma lista descompactada
