"""
isnumeric   isdigit     isdecimal
"""

n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
"""
if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
else:
    print('Nao pude converter o numero')
"""
try:  #tente executar
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
except:  # qualquer erro execute
    print('ERROR')