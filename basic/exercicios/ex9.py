cpf_original = '1689953509'
cpf = cpf_original[:-1]
cpf_novo = ''

v = 10
r = 0
total = 0
for n in cpf:
    if v >= 1:
        r = int(n) * v
        print(f'{n}*{v} = {r}')
        total += r
        v -= 1
print(f'Total: {total}')

digito1 = 11 -(total % 11)
if digito1 > 9:
    digito1 = 0
    print(f'Digito 1: {digito1}')
    cpf_novo = cpf + str(digito1)
    print(cpf_novo)

print(50*'=')
# verificar 2
v = 11
r = 0
total = 0
for n in cpf:
    if v >= 1:
        r = int(n) * v
        print(f'{n}*{v} = {r}')
        total += r
        v -= 1
print(f'Total: {total}')

digito2 = 11 -(total % 11)
print(f'Digito 2: {digito2}')
cpf_novo = cpf + str(digito2)
print(cpf_novo)

# resultado
print(50*'=')
if cpf_original == cpf_novo:
    print('Válido')
else:
    print('Inválido')