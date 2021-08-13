n = input('Digite um numero inteiro: ')
#  converter str >> int
try:
    n = int(n)
    #  iniciar pode usar isdigit()
    if n%2 == 0:
        print(f'Numero {n} e Par')
    else:
        print(f'Numero {n} e impar')
except:
    print(f'"{n}" Nao e um numero inteiro')