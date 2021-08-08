"""
conta a qnt de caractere
so funciona com str
"""

print(25*'-'+'Cadastro'+25*'-')

user = input('Usuario: ')
passwd = input('Senha: ')
r_passwd = input('Repita a senha: ')

qnt_caracteres_pass1 = len(passwd)
qnt_caracteres_pass2 = len(r_passwd)

if qnt_caracteres_pass1 and qnt_caracteres_pass2 >= 6:
    print(50*'-')
    print('Cadastrado com sucesso.')
    print(50*'-')
    print(f'nome:{user}')
    print(f'senha:{passwd}')
else:
    print(50*'-')
    print('Usuario nao cadastrado.')
    print('Voce precisa digitar 6 caracteres no minimo')