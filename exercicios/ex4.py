user = input('Usuario: ')
passwd = int(input('Senha: '))

user_db = 'xeroga'
passwd_db = 1234

if user_db == user and passwd_db == passwd:
    print('Voce esta logado no sistema.')
else:
    print('Usuario ou senha invalidos.')